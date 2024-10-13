from socket import*
HOST = gethostbyname(gethostname())

PORT = 9999
ADDR = (HOST, PORT)
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((HOST,PORT))
sentence = 'ghj'
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence.decode())
clientSocket.close()
