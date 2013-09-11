# http://bottlepy.org/docs/dev/index.html
from bottle import route, run, static_file
import service

@route('/')
def hello():
    return static_file('index.html', root='./')

	
@route('/get_limits/kml')
def get_homes():
	return service.get_limits('kml')

@route('/get_limits/json')
def get_homes():
	return service.get_limits('json')


	
@route('/get_homes/json')
def get_homes():
	return service.get_homes('json')
	
	
@route('/get_homes/geojson')
def get_homes():
	return service.get_homes('geojson')
	
@route('/get_homes/csv')
def get_homes_csv():
	return service.get_homes(format='csv')

	
@route('/:filename#.*#')
def server_static(filename):
	print 'serving... ' + filename
	return static_file(filename, root='./')	
	
run(host='localhost', port=8080, debug=True)

