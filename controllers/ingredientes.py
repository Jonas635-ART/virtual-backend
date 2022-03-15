from flask_restful import Resource, request

class IngredientesController(Resource):
   def get(self):
       return {
           'message': 'Soy el get del ingrediente'
       }
   def post(self):
       print(request.get_json())
       return {
            'message': 'Soy el post'
        }










































