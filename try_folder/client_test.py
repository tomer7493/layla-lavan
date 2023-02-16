import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 8820))
while(True):
    print("enter the command:")
    data = input()
    data= data.split()
    if (len(data)==1):
        data = data[0]+"\r\n"+"5"+"\r\n"
    else:
        data = data[0]+"\r\n"+"5"+"\r\n"+data[1]
    my_socket.send(data.encode())
    data = my_socket.recv(1024).decode()
    print("The server sent " + data)
    if data == "QUIT":
        my_socket.close()
        break   

