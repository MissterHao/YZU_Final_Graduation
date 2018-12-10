# ================================================================================
# API
# ================================================================================
from flask import Blueprint, jsonify, request
from . import DATABASE
from flask_cors import cross_origin
# app = __import__("App.server", fromlist=("servr",))
# server = app.server

api = Blueprint('ldaapi', __name__, url_prefix="/api/lda", template_folder='templates')

@api.route("/setting", methods=["POST"])
@cross_origin()
def api_lda():
    
    setting = request.json
    
    return ""







