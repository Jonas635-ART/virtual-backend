class Animal:

    def __init__(self, nombre, genero, nro_patas):

       self.nombre = nombre
       self.genero = genero 
       self.patas = nro_patas

    def descripcion(self):
        return 'es un {}, es un {}, y tengo {} patas'.format(
            self.patas, 
            self.genero, 
            self.nombre, #02
            )

foca = Animal('foca', 'm', 2)
cienpies = Animal('cienpies', 'h', 60)

print(foca.descripcion())
print(cienpies.descripcion())

























