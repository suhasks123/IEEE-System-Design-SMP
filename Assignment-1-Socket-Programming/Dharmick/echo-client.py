import socket                                           
Host = '127.0.0.1'
Port = 65432
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s: #creating socket
    s.connect((Host,Port)) #request for connection
    s.sendall(b'HELLO') #sending data to server
    data = s.recv(1024) #reciving data from server

print('Recived',repr(data)) #printing recived data

