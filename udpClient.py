from socket import *

serverPort = 13000
serverName = "10.124.6.91"
clientSocket = socket(AF_INET, SOCK_DGRAM)
fileName = input("Enter the file name ").encode()
clientSocket.sendto(fileName, (serverName, serverPort))
fileContent, serverAddr = clientSocket.recvfrom(1024)
print(fileContent.decode())
clientSocket.close()
