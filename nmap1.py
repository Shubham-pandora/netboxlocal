import socket

import platform
# print(platform.node())
# print(socket.gethostname())
# print(socket.gethostbyaddr("192.168.3.119"))
# a = socket.gethostbyaddr("192.168.2.139")
a = socket.gethostbyaddr("192.168.2.32")
# print(type(a))
print(a[0])


# import nmap
# nmScan = nmap.PortScanner()

# nmScan.scan('192.168.1.32', '21-443')
# nmScan.command_line()