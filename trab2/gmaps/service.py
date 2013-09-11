# -*- coding: utf-8 -*-
import geojson
import simplejson
import sqlite3
import os


def get_homes(format='json'):
	path =  os.path.dirname(os.path.abspath(__file__))

	con = sqlite3.connect(path+'\\zap.db' )
	con.row_factory = sqlite3.Row

	print 'Quering home'
	rows = con.execute('select id_home, price_m2,  condo, bedrooms, suites, garage, lat_home, lng_home, glat, glng from vw_price_m2 where lat_home is not null ').fetchall()

	if format=='json':
		homes = []
		lat,lng,price_m2,id_home = None,None,None,None
		for row in rows:
			point = {
				'lat':row['lat_home'], 
				'lng': row['lng_home'], 
				'price_m2':row['price_m2'],
				'id_home': row['id_home']}
			print point
			homes.append(point)
		con.close()
		return simplejson.dumps(homes)
	

	if format=='geojson':
		features = []
		for row in rows:
			point = geojson.Point(coordinates=[row['lat_home'],row['lng_home']])
			prop = {'price_m2':row['price_m2']}
			feature = geojson.Feature(id=row['id_home'], geometry=point, properties=prop)
			features.append(feature)
		homes = geojson.FeatureCollection(features=features)
		con.close()
		return geojson.dumps(homes)
	
	if format=='csv':
		txt = ''
		for row in rows:
			txt += str(row['lat_home'])+';'+str(row['lng_home'])+';'+str(row['price_m2'])+';'+str(row['id_home'])+'\n'
			
		con.close()
		return txt
        
def get_limits(type):
    if type == 'json':
        f = open('rj.geojson')
        
    if type == 'kml':
        f = open('rj.kml')
        
    txt = f.read()
    f.close()
    return txt
		
		
if __name__ == "__main__":
	print get_homes(format='json')

