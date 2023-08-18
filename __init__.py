from flask import Flask 

def create_app(config_name): 
    app=Flask(__name__) 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sa123456@localhost/dbpublicaciones'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    app.config['JWT_SECRET_KEY'] = 'frase-secreta'
    return app