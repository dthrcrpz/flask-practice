from flask_pymongo import PyMongo

app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

class Controller():
	def sample():
		return 'h'