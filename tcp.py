from socket import*
HOST = gethostbyname(gethostname())
serverPort = 9999
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((HOST,serverPort))
sentence = input('Input some letters:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence.decode())
clientSocket.close()
