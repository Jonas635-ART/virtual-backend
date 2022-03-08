from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def estado():
    hora_del_servidor = datetime.now()
    return{
            'status': True,
            'hour': hora_del_servidor.strftime('%d/%m/%Y %H:%M:%S') 
    }     

@app.route('/clientes')
def obtener_clientes():
    return{
        'message': 'Exito'
    }



app.run(debug=True)







































