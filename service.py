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


def get( host_domain, options_str):

	url	= os.path.join( host_domain, options_str)
	print( url)

	response	= requests.get(	url)
	'''
	print( response)
	print( type( response))
	print( response.url)
	print( response.status_code)
	print( response.encoding)
#	print( response.content)
	print( len( response.text.strip()))
	print( response.text)
	'''

	return	response.text


def post( host_domain, options_str, value):

	url	= os.path.join( host_domain, options_str)
	print( url)

	response	= requests.post(
		url,
		{'result': value} )

	return	0 if response.status_code == 200 else response.status_code


def get_nda( csv_text):

	cf	= csv.reader( StringIO( csv_text))

	list_data	= [line for line in cf]
	print( list_data)

	return	np.array( list_data[1:])


def	main( argv) :

#	csv_name 	= argv[1]
	host_domain = argv[1]
#	host_port	= int( argv[2])
	options_str	= argv[2] if len( argv) > 2 else ''

	'''
	GET
	'''
	'''
	dc	= DataGiver( csv_name)
	nda	= dc.get_data()
	'''
	csv_text	= get( host_domain, options_str)
	nda			= get_nda( csv_text)
#	'''
#	print( nda)
	print( nda.shape)

	x	= nda[:, 3:-1]		# 3: exclude cols: year, month, day.
	y	= nda[:, -1]

	'''
	print( x)
	print( y)
	print( x.shape)
	print( y.shape)
	'''

	input_shape	= np.array( [len( x[0])])
#	print( input_shape)
#	print( input_shape.shape)
#	print( type( input_shape))

	input_shape	= np.expand_dims( input_shape, axis = 1)
	print( input_shape)

	mm	= ModelMLP( input_shape = (len( x[0]),))

	mm.train( x[:-1], y[:-1])		# -1: latest data.

	print( x[-1])
#	pred	= mm.predict( x)		# all data.
	pred	= mm.predict( np.expand_dims( x[-1], axis = 0))
	print( pred)

	'''
	POST
	'''
	err	= post( host_domain, options_str, pred)
	print( err)

	return	err


if __name__ == "__main__" :

	while True :
		err	= main( sys.argv)
		if True :
#		if err != 0 :
			break

#		'''
#		sleep( 60)
		'''
		datetime
		'''
