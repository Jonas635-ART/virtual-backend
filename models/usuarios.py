from config import conexion
from sqlalchemy import Column, types
from bcrypt import hashpw, gensalt

class Usuario(conexion.Model):
    __tablename__ = 'usuarios'

    id = Column(type_=types.Integer, primary_key= True, autoincrement= True)
    nombre = Column(type_=types.String(length=45))
    apellido = Column(type_=types.String(length=45))
    correo = Column(type_=types.Text(length=45), nullable=False, unique=True)
    password = Column(type_=types.Text(), nullable=False)

    def encriptar_pwd(self):
        # primero el password lo convierte en bytes
         # el metodo gensalt para generar un hash aleatorio y este se combina
        # con mi contraseñapara generar un nuevo hash y ese guardaremos en el bd
        # ahora lo convierte en string para guardarlo en la bsae de datos
         # sobre escribo el valor del password en la instancia por el generado
        password_bytes = bytes(self.password, 'utf-8')
        salt = gensalt(rounds=10)
        hash_password = hashpw(password_bytes, salt)
      
        hash_pwd_string = hash_password.decode('utf-8')
       
        self.password = hash_pwd_string
    


















































