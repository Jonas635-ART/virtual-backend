import unittest
from app import app
from datetime import datetime

class TestInicioFlask(unittest.TestCase):
    def setUp(self):
        self.nombre= 'Eduardo'
        self.aplicacion_flask = app.test_client()


    @unittest.skip('Lo salte porque solo queria jugar con este metodo setUp')
    def testNombre(self):
        self.assertEqual(self.nombre, 'Eduardo')

    def testEndpointStatus(self):
        '''deberia retornar la hora del servidor y su estado'''
        respuesta = self.aplicacion_flask.get('/status')

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.json.get('status'),True)
        self.assertEqual(respuesta.json.get('hora_del_servidor'), datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def TestLoginJWTExitoso(self):
        body = {
            'correo': 'jonasazula8901@gmail.comn',
            'pass': 'Hola123'
        }

        respuesta = self.aplicacion_flask.post('/login-jwt', json=body)
        self.assertEqual(respuesta.status_code, 200)
        self.assertNotEqual(respuesta.json.get('access_token'), None)
        
    def TestLoginJWTCredencialesIncorrectas(self):
         body = {
            'correo': 'jonasazula8901@gmail.comn',
            'pass': 'Hola123213223'
        }
         respuesta = self.aplicacion_flask.post('/login-jwt', json=body)
         # print(respuesta.json)
         self.assertEqual(respuesta.status_code, 401)
         self.assertEqual(respuesta.json.get('access_token'), None)
         self.assertEqual(respuesta.json.get('description'), 'Invalid credentials')












































