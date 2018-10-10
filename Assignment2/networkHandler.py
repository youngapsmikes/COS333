#!/usr/bin/env python

#-----------------------------------------------------------------------
# networkHandler.py
# Author: Quinn Donohue
#-----------------------------------------------------------------------

from queryClass import Query

#-----------------------------------------------------------------------
# An object that will set up communication with a server at a specified
# port

class QueryHandler (object):

	def __init__(self, ip, port):
		self._ip = ip
		self._port = port

	def test(self, query):
		query.printOut()

	def handle(self, query):

		try:
			sock = socket(AF_INET, SOCK_STREAM)
			sock.connect((self._ip, self._port))
			flo = sock.makefile(mode = 'w')
			
		except:
			print "oh no"


#-----------------------------------------------------------------------