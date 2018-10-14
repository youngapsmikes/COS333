#!/usr/bin/env python

#-----------------------------------------------------------------------
# networkHandler.py
# Author: Quinn Donohue
#-----------------------------------------------------------------------
from sys import exit, argv, stderr
from socket import socket
from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from pickle import dump
from pickle import load
from queryClass import Query

#-----------------------------------------------------------------------
# An object that will set up communication with a server at a specified
# port

class NetworkHandler (object):

	def __init__(self, ip, port):
		self._ip = str(ip)
		self._port = int(port)

	def test(self, query):
		query.printOut()

	# Take in a query object, and then communicate with the server at
	# self._ip, self._port to pass along query object. Recieve from
	# server a dictionary, return this dictionary.
	def queryHandle(self, query):

<<<<<<< Updated upstream
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((self._ip, self._port))
		
		# dumpy query object to regserver
		outFlo = sock.makefile(mode = 'w')
		dump([True], outFlo)
		dump(query, outFlo)
		outFlo.flush()
		

		# read in dictionary from regserver
		inFlo = sock.makefile(mode = 'r')
		status = load(inFlo)
		payload = load(inFlo)

		sock.close()

		if not status:
			raise payload
			return
		else:
			return payload 

	# Take in class ID, communicate classid to server, and recieve
	# a dictionary in the same format as in assignment 1 that will be
	# returned
	def searchHandle(self, classid):
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((self._ip, self._port))
		
		# dumpy query object to regserver
		outFlo = sock.makefile(mode = 'w')
		dump([False], outFlo)
		dump([classid], outFlo)
		outFlo.flush()
		
		# read in dictionary from regserver
		inFlo = sock.makefile(mode = 'r')
		status = load(inFlo)
		payload = load(inFlo)

		sock.close()

		if not status: 
			raise payload 
			return 
		else:
			return payload

def main(argv):

	query = Query('cos', None, None, None, True)
	if len(argv) != 3:
		print 'Usage: python %s host port' % argv[0]
		exit(1)
	nh = NetworkHandler(argv[1], argv[2])
	result = nh.queryHandle(query)
	print result 
	result = nh.searchHandle(9032)
	print result  

if __name__ == '__main__':
	main(argv)




#-----------------------------------------------------------------------