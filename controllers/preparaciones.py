from flask_restful import Resource, request
from models.preparaciones import Preparacion
from dtos.preparacion_dto import PreparacionRequestDTO, PreparacionResponseDTO
from config import conexion

class PreparacionController(Resource):
    def post(self):
        try:
           body = request.get_json()        
           data = PreparacionRequestDTO().load(body)
           print(data)
           nuevaPreparacion = Preparacion(**data)
           conexion.session.add(nuevaPreparacion)
           conexion.session.commit()
           respuesta = PreparacionResponseDTO().dump(nuevaPreparacion)
           return {
               'message': 'Preparacion creada exitosamente',
               'preparacion': respuesta

           }, 201

        except Exception as e:
            conexion.session.rollback()
            return {
           'message': 'Error al crear la preparacion',
           'content': e.args
       }, 400



































































