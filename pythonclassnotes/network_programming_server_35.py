#nettwork programming--all about using python language to handle computer networking requirements:
#socket --it will provide endpoint of a two way commuincation link between  two programs runnig on the network
#server:

import socket
#creating a socket
s = socket.socket()#the connection will ipv4 or ipv6
print('socket created')
#to connect with a port we have to use bind operation  with the socket as a local host
s.bind(('localhost',9999))
#we are looking request from client
s.listen(5)
print('looking for connection')
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('connection established',addr)
    #computer can understand byte language that kind of data only we can pass through a port
    c.send(bytes('hello world','utf-8'))
    print('the client name', name)
    c.close()





#alternative way:

#sockets--these are the endpoints of a bidirectional (or) two way communications channels

'''
import socket

s = socket.socket() #creating a socket object

#getting the local host name
host = socket.gethostname()

#reserving a port for our servicd
port = 9999

#binding to the port
s.bind((host,port))

print('the port has been created')

#looking any client request we have use listen
s.listen(5)
print('looking for client request')
while True:

    #establishing the connection
    c,addr = s.accept()
    message = c.recv(1024).decode()
    print('the connectiona established with',addr)
    print(message)
    c.send(bytes('yay!! connectiona has been established', 'utf-8'))
    c.close()
    # print(c)
    # print(addr)
'''
