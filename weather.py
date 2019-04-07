from __future__ import absolute_import, division, print_function, unicode_literals

'''
get weather from livedoor.
'''

import sys
import os
import requests
import json


class WeatherGiver :

	'''
	index: pref_code - 1.
	'''
	tpl_city_codes	= (
		'016010',
		'020010',
		'030010',
		'040010',
		'050010',
		'060010',
		'070010',
		'080010',
		'090010',
		'100010',
		'110010',
		'120010',
		'130010',
		'140010',
		'150010',
		'160010',
		'170010',
		'180010',
		'190010',
		'200010',
		'210010',
		'220010',
		'230010',
		'240010',
		'250010',
		'260010',
		'270000',
		'280010',
		'290010',
		'300010',
		'310010',
		'320010',
		'330010',
		'340010',
		'350010',
		'360010',
		'370000',
		'380010',
		'390010',
		'400010',
		'410010',
		'420010',
		'430010',
		'440010',
		'450010',
		'460010',
		'471010'
	)

	'''
	convert rain_pct by icon number.
		'/'	: toki doki
		'>'	: nochi
	'''
	tpl_rain_pct	= (
		0,		#  1: sunny
		20,		#  2: sunny / cloudy
		50,		#  3: sunny / rainy
		50,		#  4: sunny / snow
		10,		#  5: sunny > cloudy
		40,		#  6: sunny > rainy
		40,		#  7: sunny > snow
		50,		#  8: cloudy
		30,		#  9: cloudy / sunny
		60,		# 10: cloudy / rainy
		60,		# 11: cloudy / snow
		20,		# 12: cloudy > sunny
		70,		# 13: cloudy > rainy
		70,		# 14: cloudy > snow

		90,		# 15: rainy
		40,		# 16: rainy / sunny
		70,		# 17: rainy / cloudy
		80,		# 18: rainy / snow
		30,		# 19: rainy > sunny
		60,		# 20: rainy > cloudy
		90,		# 21: rainy > snow
		100,	# 22: heavy-rain
		90,		# 23: snow
		40,		# 24: snow / sunny
		70,		# 25: snow / cloudy
		80,		# 26: snow / rainy
		30,		# 27: snow > sunny
		60,		# 28: snow > cloudy
		90,		# 29: snow > rainy
		100,	# 30: heavy-snow
	)

	host_domain	= None
	city_code	= None

	def	__init__( self) :

		self.host_domain	= 'http://weather.livedoor.com/forecast/webservice/json/v1'
#		host_port	= ':' + argv[2]

	def get( self, pref_code):

		self.city_code	= self.tpl_city_codes[pref_code]
		options_str		= '?city={}'.format( self.city_code)

		url	= self.host_domain + options_str
#		print( url)

		'''
		get
		'''
		response	= requests.get(	url)

		'''
		parse
		'''
		dict_json	= json.loads( response.text)
		fc_today	= dict_json['forecasts'][0]

		try :
			w_temp	= fc_today['temperature']['max']['celsius']

		except :
			# instead to tomorrow value.
			w_temp	= dict_json['forecasts'][1]['temperature']['max']['celsius']

		icon_name	= fc_today['image']['url'].split( '/')[-1]
		icon_num	= int( icon_name.split( '.')[0]) - 1

		return	self.city_code, w_temp, self.tpl_rain_pct[icon_num]


def	main( argv) :

	wg	= WeatherGiver()

	city_code, w_temp, tpl_rain_pct	= wg.get( 46)

	print( "{}, {}, {}.".format(
		city_code, w_temp, tpl_rain_pct ) )


if __name__ == "__main__" :

	main( sys.argv)
