import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  
port = 12345       
server_socket.bind((host, port))
server_socket.listen(1)
print(f"Server is listening on {host}:{port}")
client_socket, address = server_socket.accept()
print(f"Connection from {address} has been established!")
client_socket.send(b"Hello from server!")
client_socket.close()
