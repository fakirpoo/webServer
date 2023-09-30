# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a server socket

serverSocket.bind(('', port))
#Fill in start
serverSocket.listen(1)

#Fill in end

while True:
	#Establish the connection

	print ('Ready to serve...')
	connectionSocket, addr = serverSocket.accept() #Fill in start -are you accepting connections?  #Fill in end

	try:
		message =connectionSocket.recv(1024)  #Fill in start -a client is sending you a message #Fill in end
		filename = message.split()[1]
		
		f = open(filename[1:])

		#opens the client requested file.
		#Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
		outputdata =f.read() #Fill in start #Fill in end
		print (outputdata)
		#Send one HTTP header line into socket
		#Fill in start#
		connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
		#Fill in end

		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()

	except Exception as e:
		# Send response message for invalid request due to the file not being found (404)
		# Remember the format you used in the try: block!
		#Fill in start
		connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
		#Fill in end
		# Close the client socket
                #Fill in start
		connectionSocket.close()
		#Fill in end
#Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
