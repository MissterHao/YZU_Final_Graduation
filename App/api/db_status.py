# ================================================================================
# API
# ================================================================================
from flask import Blueprint, jsonify
from . import DATABASE
# app = __import__("App.server", fromlist=("servr",))
# server = app.server

api = Blueprint('api', __name__, url_prefix="/api/dbstatus", template_folder='templates')

@api.route("/")
def api_f1():
    dbst = DATABASE.db_status()
    return jsonify(dbst)







