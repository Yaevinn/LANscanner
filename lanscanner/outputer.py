def printResult(queue):
    print('Found', queue.qsize(), 'opened ports')
    print('List:')
    for map in (queue.queue):
        print('IP:', map['ip'], 'PORT:', map['port'])
    print('\n')
def outputToFile(queue):
    filename = 'scanner.out'
    filecontent = '' 
    print('Saving result to', filename, 'file')
    for map in (queue.queue):
        filecontent += 'IP: ' + str(map['ip']) + ' PORT: ' + str(map['port']) + '\n'
    outFile = open (filename, 'w')
    outFile.write(filecontent)
    outFile.close()
    print('Saved!')