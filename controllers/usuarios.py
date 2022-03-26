from flask_restful import Resource, request
from dtos.registro_dto import RegistroDTO
from models.usuarios import Usuario
from config import conexion

class RegistroController(Resource):
    def post(self):
     body = request.get_json()
     try:
        data = RegistroDTO().load(body)
        nuevoUsuario = Usuario(**data)
        # generar un hash de la contraseña
        conexion.session.add(nuevoUsuario)
        conexion.session.commit()
        return {
            'message': 'Usuario registrado exitosamente'
        }, 201
     except Exception as e:
        return {
            'message': 'Error al registrar ususario',
            'content': e.args
        }, 400























