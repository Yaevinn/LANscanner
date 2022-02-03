import ipcalc

def translateTextListToList(text):
    try:
        portList = text.split(',')
        return [int (i) for i in portList]
    except:
        return []
def networkValidate(ip):
    try:
        ipcalc.Network(ip)
        return True
    except:
        return False