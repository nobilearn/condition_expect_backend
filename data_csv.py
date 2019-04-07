"""
ndarray dataset creater by csv.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import pandas as pd


class DataGiver :

	pd_df	= None

	def	__init__( self, csv_name) :

		self.pd_df	= pd.read_csv( csv_name,
								   encoding	= "utf-8" )
#								   skiprows	= 1 )

#		print( self.pd_df)
#		print( self.pd_df[:1])
#		print( self.pd_df.values)

#		self.pd_df.to_json( csv_name + '.json')


	def	get_data( self) :

		return	self.pd_df.values


def	main( argv) :

	csv_name 	= argv[1]

	dc	= DataGiver( csv_name)

	nda	= dc.get_data()
#	print( nda)
	print( nda.shape)


if __name__ == "__main__" :

	main( sys.argv)
