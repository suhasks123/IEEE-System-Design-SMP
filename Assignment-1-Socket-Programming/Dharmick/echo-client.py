import socket                                           
Host = '127.0.0.1'
Port = 65432
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((Host,Port))
    s.sendall(b'HELLO')
    data = s.recv(1024)

print('Recived',repr(data))

