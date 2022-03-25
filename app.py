from re import A
from flask import Flask, render_template

app = Flask(__name__)
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

if(__name__ == '__main__'):    
    app.run(debug=True)























