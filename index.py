from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

# CONFIGS
app.config['SECRET_KEY'] = '55624c5d52e6ce37d082dc559b5ae357'
app.config["MONGO_URI"] = "mongodb://localhost:27017/flask_practice"

# CONTROLLERS
from controllers.UserController import UserController

@app.route('/', methods=['GET', 'POST'])
def start():
	controller = UserController
	if request.method == 'GET':
		return controller.index()
	elif request.method == 'POST':
		return controller.store()

if __name__ == '__main__':
	app.run(debug=True)