from config import validador
from marshmallow import fields

class PaginacionRequestDTO(validador.Schema):
    page = fields.Integer(required=False, load_defult=1)
    PerPage = fields.Integer(required=False, load_default=10)








































