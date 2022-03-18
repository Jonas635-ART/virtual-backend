from flask_restful import Resource, request
from models.recetas import Receta
from dtos.receta_dto import RecetaRequestDTO

class RecetasController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = RecetaRequestDTO().load(body)

            return {
                'message':'Receta exitosamente creada'
            }, 201

        except Exception as e:
            return {
                'message':'Error al crear la receta',
                'content': e.args
            }











































