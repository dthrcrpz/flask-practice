from flask import Flask, render_template, jsonify

app = Flask(__name__)

# CONFIGS
app.config['SECRET_KEY'] = '55624c5d52e6ce37d082dc559b5ae357'
app.config["MONGO_URI"] = "mongodb://localhost:27017/flask_practice"

# INITIALIZE ROUTES
from routes import Routes
init_routes = Routes(app)

if __name__ == '__main__':
	app.run(debug=True)