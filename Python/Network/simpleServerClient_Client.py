#coding = utf-8
__author__ = 'aresowj'

'''
A simple server-client sample using socket connection.
This is the client side script.
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

print(s.recv(1024).decode('utf-8'))		#Print the welcome message
for data in [b'Ares', b'Dale', b'Sun']:
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
