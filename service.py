"""
ndarray dataset creater by csv.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import sys

import numpy as np

from data_csv import DataGiver
from model import ModelMLP


def	main( argv) :

	csv_name 	= argv[1]

	dc	= DataGiver( csv_name)

	nda	= dc.get_data()
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
	print( input_shape)
	print( input_shape.shape)
	print( type( input_shape))

	input_shape	= np.expand_dims( input_shape, axis = 1)
	print( input_shape)

#	sys.exit( 0)

	mm	= ModelMLP( input_shape = (6,))

	mm.train( x[:-1], y[:-1])

	print( x[-1])
#	pred	= mm.predict( x)
	pred	= mm.predict( np.expand_dims( x[-1], axis = 0))
	print( pred)


if __name__ == "__main__" :

	main( sys.argv)
