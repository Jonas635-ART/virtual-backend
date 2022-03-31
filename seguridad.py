from config import conexion
from models.usuarios import Usuario
from bcrypt import checkpw

def autenticador(username, password):
    """ Funcion encargada de validar si las credenciales son correctas o no, si no son pasara, 
    pero si lo son retornara un JWT"""
    # Priemro valida si los parametros son correctos
    if username and password:
        # Buscare el usuario en la bd
        usuarioEncontrado = conexion.session.query(Usuario
        ).filter_by(correo=username).first()
        if usuarioEncontrado:
            print('se encontro el usuario')
            # validar si la contraseña es correctas
            validacion = checkpw(bytes(password, 'utf-8'), bytes(usuarioEncontrado.password,'utf-8'))
            if validacion is True:
                print('si es la contraseña')
                # si todas las validaciones son correctas, debemos retornar un objeto con el atributo ID
                return usuarioEncontrado
            else:
                return None
        else: 
            return None
    else:
        return None        

def identificador (payload):
    """Sirve para validar al ususario previamente autenticado"""
    # en el payload se obtiene la parte intermedia de la JWT la informacion que se puede visualizar sin saber la contraseña de la token.
    #identity -> la identificacion del usuario (en general viene a ser el ID del mismo)
    print(payload)
    usuarioEncontrado : Usuario | None = conexion.session.query(Usuario).filter_by(id=payload['identity']).first()
    if usuarioEncontrado:
        #esto me sirve para cuando quiera acceder al usuario actual de la peticion
        return {
            'id':usuarioEncontrado.id,
            'nombre':usuarioEncontrado.nombre,
            'correo':usuarioEncontrado.correo
        }
    else:
        return None












































