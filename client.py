import socket

HEADER= 64
FORMAT='utf-8'
PORT=5050
DISCONNECT_MESSAGE="!DISCONNECT"
SERVER=socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(ADDR)
