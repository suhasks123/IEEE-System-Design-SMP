#import the socket library
import socket

#create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the server using connect()
s.connect((socket.gethostname(),1024))

info = ''

#a while loop to receive data of certain size each time
while True:
    # receive data from the server through recv()
    msg= s.recv(7)
    if len(msg) <= 0:
        break
    info += msg.decode("utf-8")
    #print(msg)
    print(info)