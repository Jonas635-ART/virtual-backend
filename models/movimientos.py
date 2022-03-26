from config import conexion
from sqlalchemy import Column, types, orm
from datetime import datetime
from sqlalchemy.sql.schema import ForeignKey



class Movimiento(conexion.Model):
    __tablename__ = 'movimientos'

    id = Column(type_=types.Integer, primary_key= True, autoincrement= True)
    monto = Column(type_=types.Float(), nullable=False)
    tipo = Column(type_=types.Enum('INGRESO','EGRESO'), nullable=False)
    descripcion = Column(type_=types.String(45))
    moneda = Column(type_=types.Enum('SOLES','DOLARES','EUROS'), nullable=False)
    fecha_creacion = Column(type_=types.DateTime(), default=datetime.now())


    #Relationships
    usuario_id = Column(ForeignKey(Column='usuarios_id'), 
                        type= types.Integer, nullable=False)
    usuario = orm.relationship('Usuario', backref = 'usuario_movimientos') 

    categoria_id = Column(ForeignKey(Column='categorias_id'), 
                          type= types.Integer, nullable=False)
    categoria = orm.relationship('Categoria', backref = 'categoria_movimientos') 

    






















