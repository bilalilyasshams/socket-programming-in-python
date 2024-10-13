import socket
import threading

def receive_messages(clientSocket):
    while True:
        try:
            message = clientSocket.recv(1024).decode()
            if message:
                print(message)
            else:
                break
        except:
            break

def main():
    serverName = '10.75.46.87'  # Change this to the server's IP address
    serverPort = 12005
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    name = input("Enter your name: ")
    clientSocket.send(name.encode())

    threading.Thread(target=receive_messages, args=(clientSocket,)).start()

    while True:
        message = input()
        if message:
            clientSocket.send(message.encode())
        else:
            clientSocket.close()
            break

#if _name_ == "_main_":
    #main()