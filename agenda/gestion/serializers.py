from rest_framework import serializers
from .models import Etiqueta, Tareas
# https://www.django-rest-framework.org/api-guide/serializers/
# https://www.django-rest-framework.org/api-guide/fields/

class PruebaSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=40, trim_whitespace = True)
    apellido = serializers.CharField()
    correo = serializers.EmailField()
    dni = serializers.RegexField(max_length= 8, min_length= 8, regex="[0-9]")
    # dni = serializers.IntegerField(min_value=10000000, max_value=99999999) 

class TareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'
        extra_kwargs = {
            'etiquetas': {
                'write_only': True
                }
        }
     
# Sirve para que en el caso que querramos devolver la informacion de una relacion entre este modelo podemos indicar hasta que grado de profundidad queremos que nos devuelva la informacion, la profundida maxima es de 10

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = '__all__'
        depth = 1

class EtiquetaSerializer(serializers.ModelSerializer):

    tareas = TareasSerializer(many=True, read_only=True)

    class Meta:
        model = Etiqueta
        fields = '__all__'

        extra_kwargs = {
            # 'nombre': {
            #     'write_only': True
            #     },
                        'id':{
                            'read_only': True}
                            }
        read_only_fields = ['createAt']
     













