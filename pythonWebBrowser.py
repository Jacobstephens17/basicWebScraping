# Web Browser with socket 
# import socket 
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/clown.txt HTTP/1.0\n\n'.encode()
# mysock.send(cmd)
# while True: 
#     data = mysock.recv(512)
#     if ( len(data) < 1) :
#         break 
#     print(data.decode())
# mysock.close()


# Reading Web Files with urllib

import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt')
# for line in fhand:
#     print(line.decode().strip())


# Reading Web Pages with urllib
from bs4 import BeautifulSoup
fhand = urllib.request.urlopen('http://dr-chuck.com/page1.htm')

for line in fhand:
    print(line.decode().strip())



