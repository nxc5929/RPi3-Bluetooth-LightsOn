import bluetooth

server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)

def wait_for_connect():
	port = 1
	server_sock.bind(("",port))
	server_sock.listen(1)

	global client_sock
	client_sock,address = server_sock.accept()
	print "Accepted connection from ",address

def getNext():
	data = client_sock.recv(1024)
	print "received [%s]" % data
	return data

def close():
	client_sock.close()
	server_sock.close()
