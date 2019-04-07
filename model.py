from __future__ import absolute_import, division, print_function, unicode_literals

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout


class ModelMLP :

	model	= None
	scaler	= None

	def	__init__( self, input_shape) :
		''' define mlp model. '''

#		nodes	= 512
		nodes	= 128
		d_out	= 0.2

		self.model	= Sequential()
		self.model.add( Dense( nodes, activation = 'relu', input_shape = input_shape))
		self.model.add( Dropout( d_out))
		self.model.add( Dense( nodes, activation = 'relu'))
		self.model.add( Dropout( d_out))
#		self.model.add( Dense( num_classes, activation = 'softmax'))
		self.model.add( Dense( 1))

#		self.model.summary()

#		self.model.compile(	loss		= 'categorical_crossentropy',
		self.model.compile(	loss		= 'mean_squared_error',
#							optimizer	= 'rmsprop',
							optimizer	= 'adam',
							metrics		= ['accuracy'] )

		self.scaler	= StandardScaler()

	def	get_model( self) :

		return	self.model

	def	train( self, x, y) :

		x_train, x_valid, y_train, y_valid	= train_test_split(	x, y, test_size	= .2)

		'''
		print( x_train)
		print( x_valid)
		print( y_train)
		print( y_valid)
		print( x_train.shape, x_valid.shape)
		print( y_train.shape, y_valid.shape)
		'''

		self.scaler.fit( x_train)
		x_train	= self.scaler.transform( x_train)
		x_valid	= self.scaler.transform( x_valid)

		'''
		self.model.fit(	x,
						y,
						validation_split	= 0.2,
		'''
		self.model.fit(	x_train,
						y_train,
						validation_data		= (x_valid, y_valid),
						batch_size			= 4,
						epochs				= 100,
						verbose				= 2 )

	def	predict( self, x_pred) :

#		print( "x_pred: {}".format( x_pred))

		x_pred	= self.scaler.transform( x_pred)

#		print( "x_pred: {}".format( x_pred))
#		print( "x_pred: {}".format( x_pred[-1]))
#		print( "shape : {}".format( x_pred.shape))

		return	self.model.predict( x_pred)
