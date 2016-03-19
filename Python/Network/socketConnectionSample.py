#codeing = utf-8
import socket
__author__ = 'aresowj'
#Create socket object and connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#Using IPv4 protocol
s.connect(('www.google.com', 80))

s.send(b'GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n')

buf = []
while True:
	d = s.recv(1024)	#Receive at most 1024bytes
	if d:
		buf.append(d)
	else:
		break
data = b''.join(buf)

s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('socketConnectionSample.html', 'wb') as f:
	f.write(html)	#Save the html contect
