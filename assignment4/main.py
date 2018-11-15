from sys import argv
from bottle import route, request, response, error, redirect, run
from bottle import template, TEMPLATE_PATH

from SQLExecutor import executeSearch, executeSearchClass
from queryClass import Query
from searchClass import Search

TEMPLATE_PATH.insert(0,'')

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

def genrow(value):
    return '<td align ="left">' + value + '</td>'

@route('/')
@route('/search')
def search():
    templateInfo = {}
    return template('search.tpl', templateInfo)

@route('/searchresults')
def searchResults():
    dept = request.query.get('dept')
    coursenum = request.query.get('coursenum')
    area = request.query.get('area')
    title = request.query.get('title')

    dept = preprocessKey(dept)
    coursenum = preprocessKey(coursenum)
    area = preprocessKey(area)
    title = preprocessKey(title)

    query = Query(dept = dept, coursenum = coursenum, area = area, title = title)
    d = executeSearch(query)

    print type(d["classid"][0])
    print type(genrow(d["dept"][0]))

    ret = ''
    for i in range(0, len(d[d.keys()[0]])):
        ret += ('<tr><td align="left"><a href="results/' + d["classid"][i]  + 
            '" target="_blank">' + d["classid"][i] + '</a></td>' +
            genrow(d["dept"][i]) + genrow(d["coursenum"][i]) + 
            genrow(d["area"][i]) + genrow(d["title"][i]) +
            '</tr>')

    return ret

@route('/results/<classid>')
def results(classid):
    d = executeSearchClass(classid)
    templateInfo = {
        'classid': classid,     
        'd': d}
    return template('results.tpl', templateInfo)

@error(404)
def notFound(error):
    return 'Not found'

if __name__ == '__main__':
    if len(argv) != 2:
        print 'Usage: ' + './runserver' + ' port'
        exit(1)
    run(host='0.0.0.0', port=argv[1], debug=True)
