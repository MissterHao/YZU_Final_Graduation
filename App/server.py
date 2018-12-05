from flask import Flask
from flask_cors import CORS, cross_origin

server = Flask(__name__, static_url_path='')# , static_folder="./templates", static_url_path="/Users/User/Desktop/school_project/App/templates")

cors = CORS(server)
server.config['CORS_HEADERS'] = 'Content-Type'


# View Controller
from App.views import views

# Api Serve
from App.api.db_status import api as db_status_blueprint
server.register_blueprint(db_status_blueprint)








