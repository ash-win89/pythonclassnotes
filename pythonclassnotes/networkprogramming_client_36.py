import socket

s = socket.socket()

s.connect(('localhost',9999))

s.send(bytes('this is the cliend message', 'utf-8'))
print(s.recv(1024).decode())

























'''
import socket

s=socket.socket()
#connecting with the server port
s.connect(('localhost',9998))

name = input('enter your name')
s.send(bytes(name,'utf-8'))
print(s.recv(1024))
print(s.recv(1024).decode())
'''
'''
import socket

s = socket.socket()

host = socket.gethostname()
port = 9999

s.connect((host,port))
s.send(bytes('thanks message received','utf-8'))

print(s.recv(1024).decode())#we need to define a temproary memory to store the server message(1024)

s.close()
'''