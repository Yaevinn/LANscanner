import ipcalc
from pyparsing import And
import scanner
import outputer
import threading
import time
import datetime
import argparse
import sys
import helperFunctions
from queue import Queue

### vars
portList = []
elementsToScan = 0
resultQueue = Queue()
startTime = time.time()
queueObj = Queue()
network = ''

argparser = argparse.ArgumentParser(description='LANscanner script')
argparser.add_argument('-n', '--network', type=str, required=True)
argparser.add_argument('-p', '--singleport', type=int)
argparser.add_argument('-l', '--rangeLowestPort', type=int)
argparser.add_argument('-m', '--rangeHighestPort', type=int)
argparser.add_argument('-k', '--listofports', type=str)
argparser.add_argument('-t', '--threads', type=int, default=150)
argparser.add_argument('--fileoutput', dest='outfile', action='store_true')
argparser.add_argument('--no-fileoutput', dest='outfile', action='store_false')
argparser.set_defaults(outfile=False)
args = argparser.parse_args()

if args.threads > 0 and args.threads <= 150:
    threads = 10 # numer of threads
else:
    print('Number of threads should be in range 1 - 150')
    sys.exit()

if helperFunctions.networkValidate(args.network):
    network = args.network
else:
    print('Bad network!')
    sys.exit()

threads = args.threads

if args.listofports is not None:
    portList = helperFunctions.translateTextListToList(args.listofports)
    if not portList:
        print('Bad port list!')
        sys.exit()
elif args.rangeLowestPort is not None and args.rangeHighestPort is not None:
    portList = range(args.rangeLowestPort, args.rangeHighestPort + 1)
elif args.singleport is not None:
    portList = [args.singleport]
else:
    print('Please specify port correctly!')
    sys.exit()


# run scanner in threads
def threader():
   while True:
      worker = queueObj.get()
      result = scanner.portscan(worker)
      if result == True:
          resultQueue.put(worker)
      queueObj.task_done()

def queueCounter():
    while(True):
        time.sleep(5)
        progressPercentage = round((elementsToScan - queueObj.qsize()) / elementsToScan * 100, 2)
        remainSeconds = round((time.time() - startTime) * 100 / progressPercentage - (time.time() - startTime))
        print('Scanning... Progress:', progressPercentage, '% Remain', remainSeconds, 'seconds')

def queueCounterThread():
    thr = threading.Thread(target = queueCounter)
    thr.daemon = True
    thr.start()

# Create threads 
for i in range(threads):
    thr = threading.Thread(target = threader)
    thr.daemon = True
    thr.start()

# Count elements to scan
for ip in ipcalc.Network(network):
    for port in portList:
        elementsToScan += 1

# Generate ip + port maps and put to queue
for ip in ipcalc.Network(network):
    for port in portList:
        queueObj.put({'ip': ip, 'port': port})

print('-----------------------------')
print('\nAll elements to scan:', elementsToScan)
print('Scan started at', datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print('-----------------------------')
queueCounterThread()

queueObj.join()

print('\n\n-----------------------------')
print('Scan completed in', round(time.time() - startTime, 2), 'seconds')
outputer.printResult(resultQueue)

if args.outfile == True:
    outputer.outputToFile(resultQueue)