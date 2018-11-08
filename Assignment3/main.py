from sys import argv
from bottle import route, request, response, error, redirect, run
from bottle import template, TEMPLATE_PATH

from SQLExecutor import executeSearch, executeSearchClass
from queryClass import Query
from searchClass import Search



# any additional error handling?
def preprocessKey(key):
    if (key is None) or (key.strip() == ''):
        return ''
    return key 

def preprocessPrev(input):
    if input is None:
        input = ''
        return input 
    return input 

@route('/')
@route('/search')
def search():

    prevdept = preprocessPrev(request.get_cookie('prevDept'))
    prevcoursenum = preprocessPrev(request.get_cookie('prevNum'))
    prevarea = preprocessPrev(request.get_cookie('prevArea'))
    prevtitle = preprocessPrev(request.get_cookie('prevTitle'))
    
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
        'prevdept': prevdept,   
        'd': results}
    return template('search.tpl', templateInfo)

@route('/search2')
def search2():
    prevdept = preprocessPrev(request.get_cookie('prevDept'))
    prevcoursenum = preprocessPrev(request.get_cookie('prevNum'))
    prevarea = preprocessPrev(request.get_cookie('prevArea'))
    prevtitle = preprocessPrev(request.get_cookie('prevTitle'))
    
    query = Query(dept = prevdept, coursenum = prevcoursenum, area = prevarea, title = prevtitle)
    results = executeSearch(query)

    templateInfo = {
        'dept': prevdept, 
        'coursenum': prevcoursenum, 
        'area': prevarea, 
        'title': prevtitle,  
        'd': results}
    return template('search.tpl', templateInfo)


@route('/results/<classid>')
def results(classid):
    d = executeSearchClass(classid)
    templateInfo = {
        'classid': classid,     
        'd': d}
    return template('results.tpl', templateInfo)


## saving the search form results

if __name__ == '__main__':
    if len(argv) != 2:
        print 'Usage: ' + argv[0] + ' port'
        exit(1)
    run(host='0.0.0.0', port=argv[1], debug=True)
