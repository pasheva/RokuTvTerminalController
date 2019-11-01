import socket

SOCKET = ('239.255.255.250', 1900)

HTTP_REQUEST = '''\
M-SEARCH * HTTP/1.1\r\n\
Host: %s:%s\r\n\
Man: "ssdp:discover"\r\n\
ST: roku:ecp\r\n\r\n\
''' % SOCKET

HTTP_REQUEST_AS_BYTES = HTTP_REQUEST.encode()

def find_roku():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(HTTP_REQUEST_AS_BYTES, SOCKET)
    data = s.recv(1024)
    return data

a = find_roku().decode('utf-8')
print(a)


"""
HTTP/1.1 200 OK
Cache-Control: max-age=3600
ST: roku:ecp
USN: uuid:roku:ecp:YK00R3943995
Ext: 
Server: Roku UPnP/1.0 Roku/9.1.0
LOCATION: http://192.168.0.8:8060/
device-group.roku.com: 6DB2C0C479BE68FE60B4
WAKEUP: MAC=2c:d9:74:b7:ad:00;Timeout=10
"""

