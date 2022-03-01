nombre = 'jose'

print(nombre)
# Concatenar o juntar varios valores
print('el nombre es:',nombre,'del usuario')

estado_civil = 'viudo'

# Para usar el metodo format hay que coindir los datos con el {}
print('La persona {} es {}'.format(nombre, estado_civil))

print('{1} es una persona {0}'.format(estado_civil, nombre))