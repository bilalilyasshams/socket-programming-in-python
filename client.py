import socket

HEADER = 64
PORT = 9999
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "your_server_ip_here"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

# Set the client name
name = input("Enter your name: ")
send(name)  # Send the name first

# Example usage:
while True:
    message = input("Message: ")
    if message == DISCONNECT_MESSAGE:
        send(DISCONNECT_MESSAGE)
        break
    send(message)
