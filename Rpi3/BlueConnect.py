import bluetooth

#sets server socket to RFCOMM. RF to Serial
server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

#Waits for a bluetooth client to attempt to connect and joins the connection
def wait_for_connect():
	port = 1
	server_sock.bind(("",port))
	server_sock.listen(1)

	#Accepts the connection
	global client_sock
	client_sock,address = server_sock.accept()
	print "Accepted connection from ",address

#Gets the last string sent by the
def getNext():
	data = client_sock.recv(1024)
	print "received [%s]" % data
	return data

#closes the connection
def close():
	client_sock.close()
	server_sock.close()
