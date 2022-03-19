from flask_restful import Resource, request
from models.recetas import Receta
from dtos.receta_dto import RecetaRequestDTO, RecetaResponseDTO
from config import conexion
class RecetasController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = RecetaRequestDTO().load(body)
            nuevaReceta = Receta(
                nombre = data.get('nombre'),
                estado = data.get('estado'),
                comensales = data.get('comensales'),
                duracion = data.get('duracion'),
                dificultad = data.get('dificultad')
            )
         
            conexion.session.add(nuevaReceta)
            conexion.session.commit()
            
            respuesta = RecetaResponseDTO().dump(nuevaReceta)
            return {
                'message':'Receta exitosamente creada',
                'content': respuesta
            }, 201

        except Exception as e:
            conexion.session.rollback()
            return {
                'message':'Error al crear la receta',
                'content': e.args
            }

    def get(self):
      # TODO: agrega paginacion
      recetas = conexion.session.query(Receta).all()
      respuesta = RecetaResponseDTO(many=True).dump(recetas)
      return {
        'message':'las recetas son:',
        'content': respuesta
    }
class BuscarRecetaController(Resource):
    def get(self):
        query_params = request.args
        print(query_params.get('nombre'))
        recetas = conexion.session.query(Receta).filter_by(**query_params).all()
        print(recetas)
        return {
            'message': ''
        }








































