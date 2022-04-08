from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import (  PruebaSerializer, 
                            TareasSerializer, 
                            EtiquetaSerializer, 
                            TareaSerializer,
                            TareaPersonalizableSerializer)
from .models import Etiqueta, Tareas
from rest_framework import status
from django.utils import timezone


@api_view(http_method_names=['GET', 'POST'])
def inicio(request: Request):
    # request sera toda la informacion enviada por el cliente > https://www.django-rest-framework.org/api-guide/requests/
    print(request.method)
    print(request)
    if request.method == 'GET':
        # comportamiento cuando sea GET
        return Response(data={
            'message': 'Bienvenido a mi API de agenda'
        })

    elif request.method == 'POST':
        # comportamiento cuando sea POST
        return Response(data={
            'message': 'Hiciste un post'
        }, status=201)



class PruebaApiView(ListAPIView):

    serializer_class = PruebaSerializer
    queryset = [{   'nombre': 'Jose',
                    'apellido': 'Jimenez',
                    'correo': 'jsla91@gmail.com',
                    'dni': '09098887',
                    'estado_civil': 'viudo'},
                    {   'nombre': 'Carla',
                    'apellido': 'Becerra',
                    'correo': 'Crcerra@gmail.com',
                    'dni': '23536437',
                    'estado_civil': 'soltera'}
                    ]
    def get(self, request: Request):
        informacion = self.queryset
        informacion_serializada = self.serializer_class(data=informacion, many=True)
        informacion_serializada.is_valid(raise_exception=True)
        return Response(data={
            'message': 'Hola',
            'content': informacion_serializada.dat })

class TareasApiView(ListCreateAPIView):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer
    def post(self, request: Request):
        serializador = self.serializer_class(data=request.data)
        if serializador.is_valid():
            fechaCaducidad = serializador.validated_data.get('fechaCaducidad')
            print(type(serializador.validated_data.get('fechaCaducidad')))
            importancia = serializador.validated_data.get('importancia')
            if importancia < 0 or importancia > 10:
                return Response(data={
                    'message': 'la importancia puede ser entre 0 y 10'
                }, status=status.HTTP_400_BAD_REQUEST)

            if timezone.now() > fechaCaducidad:
                return Response(data={'message': 'La fecha no puede ser menor que la fecha actual'},
                status=status.HTTP_400_BAD_REQUEST)
                 # El metodo save() se podra llamar siempre que el serializado sea un ModelSerializer y este servira para poder guardar la informacion actual del serializador en la b
                serializador.save()
                
            return Response(data=serializador.data, status=status.HTTP_201_CREATED)
        else:
            serializador.errors
            return Response(data={
            'message': 'la data no es valida', 
            'content': serializador.errors},
            status=status.HTTP_400_BAD_REQUEST)
class EtiquetasApiView(ListCreateAPIView):
    serializer_class = EtiquetaSerializer
    queryset = Etiqueta.objects.all()

class TareaApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = TareaSerializer
    queryset = Tareas.objects.all()


























