#!/usr/bin/env python

#-----------------------------------------------------------------------
# courseserver3.py
# Author: Quinn Donohue, Michael Li
#-----------------------------------------------------------------------
import sys
from sys import exit, argv, stderr
from socket import socket
from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from pickle import dump
from pickle import load
from threading import Thread 

sys.path.append('C:\\COS333\\Assignment1\\')
from queryClass import Query
from SQLExecutor import executeSearch
from SQLExecutor import executeSearchClass

class ServerThread (Thread):

    def __init__(self, sock, clientAddr):
        Thread.__init__(self)
        self._sock = sock
        self._clientAddr = clientAddr
        
    def run(self):
        try:
            print 'Spawned thread for ' + str(self._clientAddr)
            
            inFlo = self._sock.makefile(mode='r')

            isQuery = load(inFlo)

            if isQuery[0] == True:
                queryClass = load(inFlo)
                found = executeSearch(queryClass)
            else: 
                classid = load(inFlo)
                found = executeSearchClass(classid[0])

            outFlo = self._sock.makefile(mode = 'w')
            dump(True, outFlo)
            dump(found, outFlo)
            outFlo.flush()

            self._sock.close()
            print 'Closed socket for ' + str(self._clientAddr)
            print 'Exited thread for ' + str(self._clientAddr)
        except Exception, e:
            outFlo = self._sock.makefile(mode = 'w')
            dump(False, outFlo)
            dump(e, outFlo)
            outFlo.flush()
            self._sock.close()
            print 'Closed socket for ' + str(self._clientAddr)
            print 'Exited thread for ' + str(self._clientAddr)
# def handleClient(sock, clientAddr): 

#     inFlo = sock.makefile(mode = 'r')
#     queryClass = load(inFlo)

#     outFlo = sock.makefile(mode = 'w')
#     dump(queryClass._dict, outFlo)
#     outFlo.flush()

#     print 'Wrote query to' + str(clientAddr)

#-----------------------------------------------------------------------
def main(argv):

    BACKLOG = 5

    if len(argv) != 2:
        print 'Usage: python %s port' % argv[0]
        exit(1)

    try:
        port = int(argv[1])

        serverSock = socket(AF_INET, SOCK_STREAM)
        print 'Opened server socket'
        serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        serverSock.bind(('', port))
        print 'Bound server socket to port'
        serverSock.listen(BACKLOG)
        print 'Listening'

        while True:
            sock, clientAddr = serverSock.accept()
            print 'Accepted connection for ' + str(clientAddr)
            print 'Opened socket for ' + str(clientAddr)
            serverThread = ServerThread(sock, clientAddr);
            serverThread.start();
            
    except Exception, e:
        print >>stderr, 'regserver:',
        print >>stderr, e

if __name__ == '__main__':
	main(argv)
