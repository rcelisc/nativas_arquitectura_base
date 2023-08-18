from flask import Flask, jsonify, request, Blueprint
from ..commands.ping import PingCommand
from ..commands.sumar import Sumar

import os

publicaciones_blueprint = Blueprint('publicaciones', __name__)

@publicaciones_blueprint.route ('/posts/ping', methods = ['GET'])

def hacer_ping():
    ping_command = PingCommand()
    result = ping_command.execute()
    return jsonify({ 'resultado:': str(result)}) #return jsonify({ 'respuesta': str(result), 'version': os.getenv("VERSION") })

@publicaciones_blueprint.route('/sum', methods = ['POST'])
def sum():
    json = request.get_json()
    result = Sumar(json['x'], json['y']).execute()
    return jsonify({ 'la suma es: ': str(result)})

