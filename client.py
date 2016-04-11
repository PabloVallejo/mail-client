#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Email client.
#
# This is a simple scripts that connes via ssl to gmail server,
# authenticates and sends a message from it to a recipient.
#
# In order to run it, you need to have a Gmail account and
# generate an App password at:
#
# https://security.google.com/settings/security/apppasswords
#
#
from socket import *
import ssl

# Email message.
msg = '\r\n Sample message from Poligran Networks student!'
endmsg = '\r\n.\r\n'

mail_server = 'smtp.gmail.com'
client_socket = socket(AF_INET, SOCK_STREAM)

# Client socket.
# Establish TCP connection with mail server
client_socket = ssl.wrap_socket(client_socket)
client_socket.connect((mail_server, 465))
recv = client_socket.recv(1024)
print recv
if recv[:3] != '220':
	print '220 reply not received from server.'

# Send HELO command and print server response.
hello_command = 'EHLO localhost\r\n'
client_socket.send(hello_command)
recv1 = client_socket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Authenticate.
client_socket.send('AUTH LOGIN base64-email\r\n')
recv1 = client_socket.recv(1024)
print recv1
client_socket.send('base64-app-password\r\n')
recv1 = client_socket.recv(1024)
print recv1

# Send MAIL FROM command and print server response.
client_socket.send('MAIL FROM: <pcvallejo@poligran.edu.co>\r\n')
recv1 = client_socket.recv(1024)
print recv1
if recv1[:3] != '250': #if the data is not received
	print '250 reply not received from server.'

# Send RCPT TO command and print server response.
client_socket.send('RCPT TO: <pabloninety@gmail.com> \r\n')
recv1 = client_socket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send DATA command and print server response.
client_socket.send('DATA\r\n')
recv1 = client_socket.recv(1024)
print recv1
if recv1[:3] != '354':
	print '250 reply not received from server.'

# Send message data.
client_socket.send(msg)

# Message ends with a single period.
client_socket.send(endmsg)
recv1 = client_socket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'

# Send QUIT command and get server response.
client_socket.send('QUIT\r\n')
client_socket.close()