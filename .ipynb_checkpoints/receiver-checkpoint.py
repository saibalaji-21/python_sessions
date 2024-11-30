import socket
c=socket.socket(socket.AF_INET,
                socket.SOCK_STREAM)
print("Socket created!!!")
c.bind(("localhost",9999))
c.listen(3)
print("Waiting for data")
s,addr=c.accept()
data=s.recv(1024).decode()
print(f"Received data is {data}")
s.send(bytes("Data received by the server !!"
             ,"utf-8"))

