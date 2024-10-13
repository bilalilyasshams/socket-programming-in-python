from socket import*
PORT = 9999
HOST = gethostbyname(gethostname())
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((HOST,PORT))
serverSocket.listen(5)
print('The server is ready to receive')
while True:
     connectionSocket, addr = serverSocket.accept()
     
     sentence = connectionSocket.recv(1024).decode()
     #capitalizedSentence = sentence.upper()
     connectionSocket.send(sentence.encode())
     ##connectionSocket.close()
