from flask import Flask


server = Flask(__name__, static_url_path='')# , static_folder="./templates", static_url_path="/Users/User/Desktop/school_project/App/templates")

# View Controller
from App.views import views

# Api Serve
from App.api.db_status import api as db_status_blueprint
server.register_blueprint(db_status_blueprint)








