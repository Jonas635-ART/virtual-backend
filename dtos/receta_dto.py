from config import validador
from models.recetas import Receta
from marshmallow import fields, validate


class RecetaRequestDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Receta
         
class RecetaResponseDTO(validador.SQLAlchemyAutoSchema):
    class Meta:
        model = Receta

class BuscarRecetaRequestDTO(validador.Schema):
    nombre = fields.String(required=False)
    estado = fields.Boolean(required=False)
    comensales = fields.Integer(required=False)
    dificultad = fields.String(required=False, validate=validate.ContainsOnly(choices=['FACIL', 'INTERMEDIO', 
    'DIFICIL', 'EXTREMO']))





































