from dotenv import load_dotenv
from flask import Flask, jsonify
from .src.blueprints.publicaciones import publicaciones_blueprint 
from .src.errors.errors import ApiError
from .src.models.model import db
from gestion_publicaciones import create_app
import os

loaded = load_dotenv('.env.development')

#loaded = load_dotenv()
app = Flask(__name__)
app.register_blueprint(publicaciones_blueprint)

#Test de lectura de archivo y print
#load_dotenv(dotenv_path='./.env.development')
variable = os.getenv("VERSION")
print("Variable : ", variable)


#Crear la base de datos.
# app = create_app('default')
# app_context = app.app_context()
# app_context.push()
# db.init_app(app)
# db.create_all()

@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "mssg": err.description,
      "version": os.environ["VERSION"]
    }
    return jsonify(response), err.code

