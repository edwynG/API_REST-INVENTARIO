from flask import Blueprint,jsonify,abort
from src.database.data import getDataBase,getSheets
from werkzeug.exceptions import HTTPException


main = Blueprint("route_origin",__name__)

@main.route("/")
def init():
    return jsonify({"result":getSheets()})

@main.route("/<sheet>")
def Specific(sheet):
    print(sheet)
    json=getDataBase(sheet=sheet)
    if json == None : abort(404)
    return jsonify({"info":{"Category":sheet},"result":json})

@main.errorhandler(404)
def handlerError404(error):
    result = jsonify({'message': 'Page not found','status':404})
    result.status_code = 404 
    return result
    
@main.errorhandler(504)
def handlerError504():
    result= jsonify({"message":"connection timeout","status":504})
    result.status_code=504
    return result

@main.errorhandler(HTTPException)
def handler_errors(e):
    result = jsonify({"error":e.name,"message":"There was a problem on the server","status": e.code})
    return result , e.code