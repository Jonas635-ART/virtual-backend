#O. de Comparacion
numero, numero1 = 10, 20
#Igual que
print(numero == numero1)
#Mayor que 
print(numero > numero1)
# mayor igual que
print(numero >= numero1)
#Menor que 
print(numero < numero1)
# menor igual que
print(numero <= numero1)
#Diferente de
print(numero != numero1)
 
 #O. logicos
print((10>5) and (10< 20))
print((10>5) or (10< 20))

# O. de identidad
#is

#is not

#sirve
verduras = ['api', 'lechuga', 'zapallo']
verduras2 = verduras
verduras3 = ['api', 'lechuga', 'zapallo']

verduras[0] = 'perejil'
verduras[1] = 'mango'
# el metodo copy() hace una copia del contenido de la variable pero se 
# guarda en una nueva posicion de la memoria
verduras4 = verduras.copy()
verduras4[0] = 'huacatay'
print(verduras2 is verduras)
print(verduras)
print(verduras2)
print(verduras3 is verduras)


print('la posicion de la variable verduras:',id(verduras))
print('la posicion de la variable verduras:',id(verduras2))
print('la posicion de la variable verduras:',id(verduras4))

# Al hablas de variables basicas al hacer la copia comparten el mismo espacio en la 
# memoria al modificarla python le asigna un nuevo espacio
nombre='jose'
nombre2 = 'carlos'
print(nombre2 is nombre)
print(id(nombre2))
print(id(nombre))
nombre2 = 1
print(nombre)
print(id(nombre2))
print(id(nombre))

#validar si el nombre es eduardo y colombiano o japones
nombre='eduardo'
pais='japones'
print(nombre == 'eduardo' and (pais == 'japones' or pais == 'colombia'))








