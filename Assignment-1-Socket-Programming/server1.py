import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))
s.listen(5)
while True :
    clt, adr=s.accept()
    print(f'Successfully connected to {adr}  ')
    clt.send(bytes("This is socket programming", "utf-8"))
    clt.close()
