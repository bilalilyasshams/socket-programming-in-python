from socket import*
from datetime import datetime
PORT = 9999
HOST = gethostbyname(gethostname())
ADDR = (HOST, PORT)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((HOST,PORT))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
     connectionSocket, ADDR = serverSocket.accept()
     
     sentence = connectionSocket.recv(1024).decode()
     #capitalizedSentence = sentence.upper()
     connectionSocket.send(datetime.today().strftime('%Y-%m-%d %H:%M:%S').encode())
     connectionSocket.close()

