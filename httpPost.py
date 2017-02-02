# This is a simple HTTP POST example
print("This is a simple HTTP POST example")
# SVCTE Cyber Security Blog site
# Original Source from Sam Bowne - "Python Scripting for Cybersecurity Professionals"
# https://samsclass.info/124/WITC2017-124-NETLAB.shtml
#
# Updated to work in Python3
#
#POST data captured from WireShark

# req = """POST /python/login1.php HTTP/1.1
# Host: attackdirect.samsclass.info
# User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate
# Cookie: __cfduid=db6c816ea61f81fb45ce824bb536a83381483659159
# Connection: keep-alive
# Upgrade-Insecure-Requests: 1
# Content-Type: application/x-www-form-urlencoded
# Content-Length: 7
# 
# u=a&p=b"""
#
req = """POST /python/login1.php HTTP/1.1
Host: attackdirect.samsclass.info
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Cookie: __cfduid=db6c816ea61f81fb45ce824bb536a83381483659159
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 7

u=a&p=b"""
#
# Updated to work in Python3
# but the POST test needs to have the "Accept-Encoding: gzip, deflate" line removed.
# I'm sure I can find the string formating to let the GZIP data print... 
# but I'm new to python3 and have not figured it out yet 
import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("attackdirect.samsclass.info", 80))
s.send((req).encode()) 
print(s.recv(1024).decode())
s.close()
#
# Code Example for Python 2.7 - still use the req variable
# import socket
# socket.setdefaulttimeout(2)
# s = socket.socket()
# s.connect(("attackdirect.samsclass.info", 80))
# s.send((req)) 
# print(s.recv(1024))
# s.close()
