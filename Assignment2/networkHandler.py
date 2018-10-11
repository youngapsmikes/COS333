#!/usr/bin/env python

#-----------------------------------------------------------------------
# networkHandler.py
# Author: Quinn Donohue
#-----------------------------------------------------------------------

from queryClass import Query

#-----------------------------------------------------------------------
# An object that will set up communication with a server at a specified
# port

class NetworkHandler (object):

	def __init__(self, ip, port):
		self._ip = ip
		self._port = port

	def test(self, query):
		query.printOut()

	# Take in a query object, and then communicate with the server at
	# self._ip, self._port to pass along query object. Recieve from
	# server a dictionary, return this dictionary.
	def queryHandle(self, query):

		try:
			sock = socket(AF_INET, SOCK_STREAM)
			sock.connect((self._ip, self._port))
			flo = sock.makefile(mode = 'w')
			
		except:
			print "oh no"


	# Take in class ID, communicate classid to server, and recieve
	# a dictionary in the same format as in assignment 1 that will be
	# returned
	def searchHandle(self, classid):



#-----------------------------------------------------------------------