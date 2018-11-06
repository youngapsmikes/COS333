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


# what does the @route stuff do 
# i kinda get that it basically creates some 
# sort of webpage with a specific path name 
# that's output is related to the code within 
# the function that it's wrapped around 

# the requests.query.get() retrieve strings from the 
# parameters in the url 

def getAmPm():
    if strftime('%p') == "AM":
        return 'morning'
    return 'afternoon' 
    
def getCurrentTime():
    return asctime(localtime())

@route('/')
@route('/index')
def index():
 
    templateInfo = {
        'ampm': getAmPm(),
        'currentTime': getCurrentTime()}
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
        'ampm': getAmPm(),
        'currentTime': getCurrentTime(),
        'errorMsg': errorMsg,
        'prevAuthor': prevAuthor}
    return template('searchform.tpl', templateInfo)
    
@route('/searchresults')
def searchResults():
    
    # search results is called by the html markup code within the 
    # search form template - this issues the get request i think
    # get the author state information from the parameters passed in from the 
    # url 
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
        'ampm': getAmPm(),
        'currentTime': getCurrentTime(),
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
