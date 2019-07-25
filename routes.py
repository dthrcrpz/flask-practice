from flask import request
from controllers.Index import Controllers

class Routes:
	def __init__(self, app):
		@app.route('/users', methods=['GET', 'POST'])
		def start():
			controller = Controllers.UserController
			if request.method == 'GET':
				return controller.index()
			elif request.method == 'POST':
				return controller.store()