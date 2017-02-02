# This is a simple HTTP request example
print("This is a simple HTTP request example")
# SVCTE Cyber Security Blog site
# Original Source from Sam Bowne - "Python Scripting for Cybersecurity Professionals"
# https://samsclass.info/124/WITC2017-124-NETLAB.shtml
#
# Updated to work in Python3

import socket
socket.setdefaulttimeout(2)
s = socket.socket()

target = input('Input Target host URL: (like www.ccsf.edu):') 
tport = 80

s.connect((target, tport))
s.send(('HEAD / HTTP/1.1\nHost: ' + target + '\n\n').encode()) 

print(s.recv(1024).decode())
s.close()

# Code Example for Python 2.7
# import socket
# socket.setdefaulttimeout(2)
# s = socket.socket()
# 
# target = raw_input('Input Target host URL: (like www.ccsf.edu):') 
# tport = 80
# 
# s.connect((target, tport))
# s.send(('HEAD / HTTP/1.1\nHost: ' + target + '\n\n')) 
# 
# print s.recv(1024)
# s.close()
