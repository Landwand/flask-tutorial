#https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/

import os

from flask import Flask

def create_app(test_config=None):
	#create & configure App
	app = Flask(__name__, instance_relative_config=True)
	#creates the flask Instance
	'''__name__ = current Py module. Tells app where it's located to set up 
	paths'''

	app.config.from_mapping(
		#sets some default configs
		SECRET_KEY='dev',
		#used by Flask & extensions to safeguard data. Set to Dev
		# as a convenient value, but will be overwritten during
		#deployment
		DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
		)
		#path for SQLite DB. It's under app.instance_path; the same
		# path that Flask has chosen for the Instance-folder

	if test_config is None:
		#load the instance config, if it exists, when not testing
		app.config.from_pyfile('config.py', silent=True)
		#overrides default config with values from config.py file in the
		#instance-folder if it exists. Example: when deploying, this
		# can be SECRET_KEY
	else:
		#load the test config if passed in
		app.config.from_mapping(test_config)

	# ensure the instance folder Exists
	try: 
		os.makedirs(app.instance_path)
	except OSError:
		pass

	# from . import db
	# db.init_app(app)

	# a simple page that says Hewwo
	@app.route('/hello')
	def hello():
		return 'Hewwoo wurld!! '

	from . import db
	db.init_app(app)

	return app


