import socket
HOST = socket.gethostbyname(socket.gethostname())
PORT = 3030  
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((HOST, PORT)) 
print(f"UDP server is listening on {HOST}:{PORT}")
while True:
    data, clientAddress = serverSocket.recvfrom(1024)  
    message = data.decode()  
    numbers = message.split()  

    if len(numbers) == 2:  
        try:
            num1 = float(numbers[0])  
            num2 = float(numbers[1])  
            result = num1 + num2  
            serverSocket.sendto(str(result).encode(), clientAddress) 
        except ValueError:
            serverSocket.sendto(b"Error: Please send valid numbers.", clientAddress) 
    else:
        serverSocket.sendto(b"Error: Please send exactly two numbers.", clientAddress)
