#import the socket library
import socket

#create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(),1024))

#listen on this port
s.listen(5)

#When a client connects to the server the server is back to this listening state.
while True:
    #When a client wants to connect to the server, the server accepts the connection with accept()
    client, address = s.accept()
    print(f"Connection to client of address {address} established")
    #send data through send()
    client.send(bytes("Basic socket programming", "utf-8"))
    client.close()