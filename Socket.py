import socket
from Settings import HOST, PORT, PASS, USER

def openSocket():

	s = socket.socket()
	s.connect(HOST, PORT)
	s.send("PASS " + PASS + "\r\n") #PASS *OAUTHKEY*
	s.send("NICK" + USER + "\r\n")
	s.send("JOIN :" + CHANNEL + "\r\n")
	return s

def sendMessage(s, message):
	messageTemp = "PRIVMSG #" + CHANNEL + " :" message
	s.send(messageTemp + "\r\n")
	print("Sent: " + messageTemp)