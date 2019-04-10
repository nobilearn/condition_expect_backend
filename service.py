"""
ndarray dataset creater by csv.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import os
import numpy as np

'''
from data_csv import DataGiver
'''
import requests
import csv
from io import StringIO
#'''

from model import ModelMLP
from weather import WeatherGiver


def get( host_domain, options_str):

	url	= os.path.join( host_domain, options_str)
#	print( url)

	response	= requests.get(	url)

	return	response.text


def post( host_domain, options_str, json_dict):

	url	= os.path.join( host_domain, options_str)
#	print( url)

	response	= requests.post( url, json_dict)

	return	0 if response.status_code == 200 else response.status_code


def get_nda( csv_text):

	cf	= csv.reader( StringIO( csv_text))

	list_data	= [line for line in cf]
#	print( list_data)

#	nda	= np.array( list_data[1:])			# 1: exclude header line.
	nda	= np.array( list_data[1:14])		# for demo.
	print( nda.shape)

	return	nda.astype( np.int)


def	loop( wg, mm, host_domain) :

	'''
	GET ~ train
	'''
	'''
	dc	= DataGiver( csv_name)
	nda	= dc.get_data()
	'''
	csv_text	= get( host_domain, 'data_response/?format=csv')
	nda			= get_nda( csv_text)
	print( nda)
	sys.exit( 0)
#	'''
#	print( nda[0])
#	print( nda.shape)

	user_id		= int( nda[0][0])
	pref_code	= int( nda[0][1])
	x	= nda[:, 5:-1]		# 5: exclude cols: year, month, day.
#	y	= nda[:, -1]
	y	= np.array( (90, 70, 50, 30, 10, 50, 90, 90, 50, 10, 30, 50, 70, 90))	# for demo.

	'''
	print( x)
	print( y)
	print( x.shape)
	print( y.shape)
	print( pref_code)
	print( type(x[0][0]))
#	sys.exit( 0)
	'''

	mm.train( x, y)

	'''
	get weather info.
	'''
	city_code, w_temp, rain_pct	= wg.get( pref_code)

	'''
	predict
	'''
	today_x	= np.array(	( rain_pct,
						  w_temp,
						  0,		# steps (dummy).
						  0 ) )		# self expect (dummy).
	print( today_x)
#	pred	= mm.predict( x)		# all data.
	pred	= mm.predict( np.expand_dims( today_x, axis = 0))
	print( "pred: {}".format( pred))

	'''
	POST
	'''
	json_dict	= {
		"user_id"	: user_id,
		"rain_pct"	: rain_pct,
		"w_temp"	: w_temp,
		"m_predict"	: int( pred)
	}
	print( json_dict)

	err	= post( host_domain, 'data_create/', json_dict)
#	err	= 0					# for demo: not post result.
	print( err)

	return	err


def	main( argv) :

#	csv_name 	= argv[1]
	host_domain = argv[1]
#	host_port	= int( argv[2])
#	options_str	= argv[2] if len( argv) > 2 else ''

	wg	= WeatherGiver()

	items	= (
		'rain_pct',
		'w_temp',
		'steps',
		'self_exp'
	)
	mm	= ModelMLP( input_shape = (len( items),))

	while True :
		err	= loop( wg, mm, host_domain)
		if True :		# for demo.
#		if err != 0 :
			break

#		'''
#		sleep( 60)
		'''
		datetime
		'''


if __name__ == "__main__" :

	main( sys.argv)
