#!/usr/bin/env python

#-----------------------------------------------------------------------
# penny.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

from sys import argv
from database import Database
from time import localtime, asctime, strftime
from urllib import quote_plus
from bottle import route, request, response, error, redirect, run
from bottle import template, TEMPLATE_PATH

TEMPLATE_PATH.insert(0, '')

@route('/')
@route('/index')
def index():
    
    templateInfo = {}
    return template('index.tpl', templateInfo)
    
@route('/searchform')
def searchForm():

    errorMsg = request.query.get('errorMsg')
    if errorMsg is None:
        errorMsg = ''
    
    prevAuthor = request.get_cookie('prevAuthor')
    if prevAuthor is None:
        prevAuthor = '(None)'
    
    templateInfo = {
        'errorMsg': errorMsg,
        'prevAuthor': prevAuthor}
    return template('searchform.tpl', templateInfo)
    
@route('/searchresults')
def searchResults():
    
    author = request.query.get('author')
    if (author is None) or (author.strip() == ''):
        errorMsg = 'Please type an author name.'
        errorMsg = quote_plus(errorMsg)
        redirect('searchform?errorMsg=' + errorMsg)       
     
    response.set_cookie('prevAuthor', author)
 
    database = Database()
    database.connect()
    books = database.search(author)
    database.disconnect()
    
    templateInfo = {
        'author': author,
        'books': books}
    return template('searchresults.tpl', templateInfo)
    
@error(404)
def notFound(error):
    return 'Not found'
    
if __name__ == '__main__':
    if len(argv) != 2:
        print 'Usage: ' + argv[0] + ' port'
        exit(1)
    run(host='0.0.0.0', port=argv[1], debug=True)