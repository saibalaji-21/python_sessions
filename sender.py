import socket
s1=socket.socket(socket.AF_INET
                 ,socket.SOCK_STREAM)
s1.connect(("localhost",9999))
data=input("Enter data to send : ")
s1.send(bytes(data,"utf-8"))
print("Data sent!!")
responce=s1.recv(1024).decode()
print(responce)

#This is a comment








