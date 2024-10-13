from socket import*
serverPort = 9999
HOST = gethostbyname(gethostname())
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((HOST,serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
     connectionSocket, addr = serverSocket.accept()
     
     sentence = connectionSocket.recv(1024).decode()
     #capitalizedSentence = sentence.upper()
     connectionSocket.send(sentence.encode())
     connectionSocket.close()
