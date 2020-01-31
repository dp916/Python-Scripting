from socket import *

# Message content
msg = "\r\n I think, therefore I am."
end = "\r\n.\r\n"

# Email sender + reciever
mfrom = "dream@sleep.com"
to = "dannypham@csus.edu"

mailserver = "gaia.ecs.csus.edu"

# Create socket + establish TCP connection
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,25))

recv = clientSocket.recv(1024)
print recv

if recv [:3] != "220":
	print "220 Reply not recieved from server."


# HELO command + server response
helloCommand = "HELO World\r\n"
clientSocket.send(helloCommand)
recvh = clientSocket.recv(1024)
print recvh

if recvh[:3] != "250":
	print "250 Reply not recieved from server."


# MAIL FROM command + server response
fromCommand = "MAIL FROM: " + mfrom + "\r\n"
clientSocket.send(fromCommand)
recvf = clientSocket.recv(1024)
print recvf


# RCPT TO command + server response
rcptCommand = "RCPT TO: " + to + "\r\n"
clientSocket.send(rcptCommand)
recvr = clientSocket.recv(1024)
print recvr


# DATA command + server response
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand)
recvd = clientSocket.recv(1024)
print recvd


# Send message
clientSocket.send(msg)
clientSocket.send(end)

recvm = clientSocket.recv(1024)
print recvm


# QUIT command + server response
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand)
recvq = clientSocket.recv(1024)
print recvq
