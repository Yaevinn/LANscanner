import socket

# scan port on ip
# map param should looks like eg.: [ 'ip': '127.0.0.1', 'port': 80 ]
def portscan(map):
    ip = map['ip']
    port = map['port']
    # longer timeout -> more sensitive scanner
    # shorter timeout -> faster
    # 0.25 is optimal
    socket.setdefaulttimeout(0.25)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conn = sock.connect((str(ip), port))
        sock.close()
        return True
    except:
        return False