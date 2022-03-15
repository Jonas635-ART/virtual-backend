# factory
from faker import Faker
from random import randint, choice
#from faker.providers import internet, person, phone_number

fake = Faker()
#fake.add_provider({internet, phone_number, person})

def generar_alumnos(limite):
  for persona in range(limite):
     nombre = fake.first_name()
     apellido_paterno = fake.last_name_male()
     apellido_materno = fake.last_name_female()
     correo = fake.ascii_free_email()
     numero_emergencia = fake.bothify(text='9########')
     sql= '''
       INSERT INTO alumnos (nombre, apellido_paterno, apellido_materno, correo, numero_emergencia) VALUES
            ('%s', '%s', '%s', '%s', '%s');''' % (nombre, apellido_paterno, apellido_materno, correo, numero_emergencia)
     print(sql)

def generar_niveles():
    secciones = ['A', 'B', 'C']
    ubicaciones = ['Sotano', 'Primer Piso', 'Segundo Piso', 'Tercer Piso']
    niveles = ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto', 'Sexto']
    # iterar los niveles y en cada nivel colocar como minimo dos secciones y como maximo 3 (random_int) y luego agregar aleatoriamente la ubicacion a ese nivel
    # Primero A Segundo Piso
    # Primero B Tercer Piso
    # Segundo A Sotano
    for nivel in niveles:
                        # entre 2 hasta <= 3 (2 | 3)
        pos_secciones = randint(2, 3)
        # pos_secciones = fake.random_int(min=2, max=3)
        for posicion in range(0, pos_secciones):
            # pos_ubicacion = fake.random_int(min=0, max= 3)
            # ubicacion= ubicaciones[pos_ubicacion]
            ubicacion = choice(ubicaciones)
            seccion = secciones[posicion]
            nombre = nivel
            sql = '''INSERT INTO niveles (seccion, ubicacion, nombre) VALUES
                                    ('%s', '%s', '%s');''' % (seccion, ubicacion,nombre)
            # print('Nivel', nivel)
            # print('Seccion', secciones[posicion])
            # print('Ubicacion', ubicaciones[pos_ubicacion])
            print(sql)


generar_niveles()






































