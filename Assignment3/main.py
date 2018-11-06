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
        'dept': dept, 
        'coursenum': coursenum, 
        'area': area, 
        'title': title,     
        'd': results}
    return template('search.tpl', templateInfo)

@route('/results/<classid>')
# pass  me classid labeled as such, searchClass has a dictionary

def results(classid):

if __name__ == '__main__':
    if len(argv) != 2:
        print 'Usage: ' + argv[0] + ' port'
        exit(1)
    run(host='0.0.0.0', port=argv[1], debug=True)
