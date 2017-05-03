import socket
import sys

#internet addressing with TCP
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

try:
	mysock.bind(('',80))
	
except socket.error:
	print("Failed to bind")
	sys.exit()
	
mysock.listen(5)

while True:
	conn, addr = mysock.accept() #will wait for data
	###this will print if i type in the IP address into web browser
	print("Got a request!")c
	data = conn.recv(1000)
	if not data:
		break
	conn.sendall(data)

conn.close()
mysock.close()

#loopback IP
#127.0.0.1

#ainfo = socket.getaddrinfo(None, 1234)
#print(ainfo)
#ms.bind(ainfo[][])

#ip address right now
#10.2.116.234
