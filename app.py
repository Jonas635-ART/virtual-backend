from flask import Flask
from datetime import datetime
from flask_restful import Api
from controllers.ingredientes import IngredientesController

app = Flask(__name__)
api = Api(app=app)

@app.route('/status', methods=['GET'])
def status():
    return {
      'status': True,
      'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

api.add_resource(IngredientesController, '/ingredientes', '/ingrediente')


if __name__ == '__main__':
    app.run(debug=True)

print('hola')











































































