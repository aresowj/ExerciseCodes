#coding = utf-8
__author__ = 'aresowj'

'''
A simple server-client sample using socket connection.
This is the server side script.
'''

import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 9999))		#Binding port 9999 on localhost
s.listen(5)		#The parameter sets the max number of waiting connections
print('Waiting for connection...')

def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s!' % data).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.' % addr)

while True:
	#Accept a connection. The socket must be bound to an address and listening for connections.
	#The return value is a pair (conn, address) 
	#where conn is a new socket object usable to send and receive data on the connection,
	#and address is the address bound to the socket on the other end of the connection.
	sock, addr = s.accept()
	
	#Create new thread to process requests.
	#The server will not be able to process multiple requests without multi-threads.
	t = threading.Thread(target=tcplink, args=(sock, addr))		#Passing the target method tcplink, using two args
	t.start()

