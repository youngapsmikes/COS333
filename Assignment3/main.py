from sys import argv
from bottle import route, request, response, error, redirect, run
from bottle import template, TEMPLATE_PATH

from SQLExecutor import executeSearch
from queryClass import Query



# any additional error handling?
def preprocessKey(key):
    if (key is None) or (key.strip() == ''):
        return ''
    return key 

@route('/')
@route('/index')
@route('/search')
def search():
    errorMsg = request.query.get('errorMsg')
    if errorMsg is None:
        errorMsg = ''
    
    dept = preprocessKey(request.query.get('dept'))
    coursenum = preprocessKey(request.query.get('coursenum'))
    area = preprocessKey(request.query.get('area'))
    title = preprocessKey(request.query.get('title'))

    # response.set_cookie('prevDept', dept)
    # response.set_cookie('prevNum', coursenum)
    # response.set_cookie('prevArea', area)
    # response.set_cookie('prevTitle', title)

    query = Query(dept = dept, coursenum = coursenum, area = area, title = title)
    results = executeSearch(query)

    templateInfo = {
        'errorMsg': errorMsg, 
        'd': results}
    return template('search.tpl', templateInfo)

@route('/search')
def search():
    dept = preprocessKey(request.query.get('dept'))
    coursenum = preprocessKey(request.query.get('coursenum'))
    area = preprocessKey(request.query.get('area'))
    title = preprocessKey(request.query.get('title'))

    response.set_cookie('prevDept', dept)
    response.set_cookie('prevNum', coursenum)
    response.set_cookie('prevArea', area)
    response.set_cookie('prevTitle', title)

    query = Query(dept = dept, coursenum = coursenum, area = area, title = title)
    results = executeSearch(query)

    templateInfo = {
        'd': results}
    return template('searchresults.tpl', templateInfo)

if __name__ == '__main__':
    if len(argv) != 2:
        print 'Usage: ' + argv[0] + ' port'
        exit(1)
    run(host='0.0.0.0', port=argv[1], debug=True)

# @route('/searchresults')
# def searchResults():
#     author = request.query.get('author')
#     if (author is None) or (author.strip() == ''):
#         errorMsg = 'Please type an author name.'
#         errorMsg = quote_plus(errorMsg)
#         redirect('searchform?errorMsg=' + errorMsg)       
     
#     response.set_cookie('prevAuthor', author)
 
#     database = Database()
#     database.connect()
#     books = database.search(author)
#     database.disconnect()
    
#     templateInfo = {
#         'author': author,
#         'books': books}
#     return template('searchresults.tpl', templateInfo)