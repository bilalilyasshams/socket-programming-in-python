from socket import*
HOST = gethostbyname(gethostname())
PORT = 9999
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((HOST,PORT))
sentence = input('Input some letters:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence.decode())
clientSocket.close()
