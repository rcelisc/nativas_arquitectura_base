from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
#from .model import  Model

db = SQLAlchemy()

# Definicion de campos
class Publicacion(db.Model):
    __tablename__ = 'publicacion'
    id = db.Column(db.String(50), primary_key=True) #identificador del usuario en formato uuid 4.
    routeId = db.Column(db.String(50)) #identificador del trayecto
    userId = db.Column(db.String(50)) #identificador del usuario dueño de la publicación
    expireAt = db.Column(db.DateTime) #fecha y hora máxima en que se reciben ofertas
    createdAt = db.Column(db.DateTime) #fecha y hora de creación de la publicación

# Constructor
def __init__(self, id, routeId, userId, expireAt, createdAt):
    #Model.__init__(self)
    self.id = id
    self.routeId = routeId
    self.userId = userId
    self.expireAt = expireAt
    self.createdAt = createdAt

# Defincion de campos para la serializacion JSON.
class PublicacionJsonSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Publicacion
        include_relationships = True
        load_instance = True

    # id = fields.String()
    # userId = fields.String()
    # expireAt = fields.String()
    # createdAt = fields.DateTime()
    # routeId = fields.DateTime()



