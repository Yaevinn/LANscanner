import ipcalc
import scanner
import threading
from queue import Queue

### vars
network = '192.168.1.0/24' # network with mask
portList = [80, 443] # list of ports
threads = 150 # numer of threads

queueObj = Queue()

# run scanner in threads
def threader():
   while True:
      worker = queueObj.get()
      scanner.portscan(worker)
      queueObj.task_done()

# Create threads 
for i in range(threads):
    thr = threading.Thread(target = threader)
    thr.daemon = True
    thr.start()

# Generate ip + port maps and put to queue
for ip in ipcalc.Network(network):
    for port in portList:
        queueObj.put({'ip': ip, 'port': port})
queueObj.join()