import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))
message = client_socket.recv(1024)
print("Received from server:", message.decode())
client_socket.close()
