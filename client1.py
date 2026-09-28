import socket

client_socket = socket.socket()
client_socket.connect(('localhost', 3000))

while True:
    msg = input("You: ")
    client_socket.send(msg.encode())
    response = client_socket.recv(1024).decode()

    print("Server: ", response)