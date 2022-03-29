from flask import Flask, render_template
import flask_cors
from flask_restful import Api
from controllers.usuarios import RegistroController, LoginController
from config import validador, conexion
from os import environ
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app=app)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

api = Api(app=app)
validador.init_app(app)
conexion.init_app(app)

conexion.create_all(app=app)


@app.route('/')
def inicio():
    return render_template('inicio.jinja', nombre='Eduardo', dia='Jueves', integrantes=[
    'pepe',
    'jose',
    'lucas'],
    usuario= {
        'nombre':'Juan',
        'direccion':'Las piedras 105',
        'edad': '40'
    },
    selecciones=[{
        'nombre':'Bolivia',
        'clasificado': False
    },{
        'nombre':'Brasil',
        'clasificado': True
    },{
        'nombre':'Chile',
        'clasificado': False
    },{
        'nombre':'Uruguay',
        'clasificado': True
    }])


api.add_resource(RegistroController, '/registro')   
api.add_resource(LoginController, '/login') 

if(__name__ == '__main__'):    
    app.run(debug=True, port=8080)























