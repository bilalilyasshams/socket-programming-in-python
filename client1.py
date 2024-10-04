import socket
HOST = socket.gethostbyname(socket.gethostname())
PORT = 3030 
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
clientSocket.sendto(f"{num1} {num2}".encode(), (HOST, PORT))
result, serverAddress = clientSocket.recvfrom(1024)
print(f"The result from the server is: {result.decode()}")
clientSocket.close()
