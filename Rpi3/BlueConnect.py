import bluetooth

server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# wait for the pi to be connected to Bluetooth
def wait_for_connect():
	port = 1
	server_sock.bind(("",port))
	server_sock.listen(1)

	global client_sock
	client_sock,address = server_sock.accept()
	print "Accepted connection from ",address

# Gets the next input from Bluetooth
def getNext():
	data = client_sock.recv(1024)
	print "received [%s]" % data
	return data

# closes the sockects used for Bluetooth
def close():
	client_sock.close()
	server_sock.close()
