import socket
Host = '127.0.0.1'
Port = 65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s: #creating socket
    s.bind((Host,Port)) #binding Socket
    s.listen() #listening for connection
    conn, addr = s.accept() #accepting connection
    with conn:
        print("conected by",addr)
        while True:
            data = conn.recv(1024) #reciving data
            if not data:
                break #if no data is being recived then clossing connection
            conn.sendall(data)  #sending back recived data

