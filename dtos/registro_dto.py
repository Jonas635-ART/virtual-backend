from config import validador
from models.usuarios import Usuario
from marshmallow_sqlalchemy import auto_field
from marshmallow import validate



#DTO Objeto de transferencia de data e informacion
class RegistroDTO(validador.SQLAlchemyAutoSchema):
    correo = auto_field(validate=validate.Email())
    class Meta:
        model = Usuario

