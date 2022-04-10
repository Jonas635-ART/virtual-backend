from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import (ListAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     CreateAPIView,
                                     DestroyAPIView)
from .serializers import (PruebaSerializer,
                          TareasSerializer,
                          EtiquetaSerializer,
                          TareaSerializer,
                          TareaPersonalizableSerializer,
                          ArchivoSerializer,
                          EliminarArchivoSerializer)
from .models import Etiqueta, Tareas
from rest_framework import status
from django.utils import timezone
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from os import remove
from django.conf import settings


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
    queryset = [{'nombre': 'Jose',
                 'apellido': 'Jimenez',
                 'correo': 'jsla91@gmail.com',
                 'dni': '09098887',
                 'estado_civil': 'viudo'},
                {'nombre': 'Carla',
                 'apellido': 'Becerra',
                 'correo': 'Crcerra@gmail.com',
                 'dni': '23536437',
                        'estado_civil': 'soltera'}
                ]

    def get(self, request: Request):
        informacion = self.queryset
        informacion_serializada = self.serializer_class(
            data=informacion, many=True)
        informacion_serializada.is_valid(raise_exception=True)
        return Response(data={
            'message': 'Hola',
            'content': informacion_serializada.dat})


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


class ArchivosApiView(CreateAPIView):
    serializer_class = ArchivoSerializer

    def post(self, request: Request):
        print(request.FILES)
        queryParams = request.query_params
        carpetaDestino = queryParams.get('carpeta')
        data = self.serializer_class(data=request.FILES)
        if data.is_valid():
            print(type(data.validated_data.get('archivo')))
            archivo: InMemoryUploadedFile = data.validated_data.get('archivo')
            print(archivo.size)
            if archivo.size > (5 * 1024 * 1024):
                return Response(data={
                    'message': 'Archivo muy grande, no mas de 5MB'
                }, status=status.HTTP_400_BAD_REQUEST)

            resultado = default_storage.save(
                (carpetaDestino+'/' if carpetaDestino is not None else '') + archivo.name, ContentFile(archivo.read()))
            print(resultado)
            return Response(data={
                'message': 'Archivo guardado exitosamente',
                'content': {
                    'ubicacion': resultado
                }},
                status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Error al subir el archivo',
                'content': data.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class EliminarArchivoApiView(DestroyAPIView):
    serializer_class = EliminarArchivoSerializer

    def delete(self, request: Request):
        data = self.serializer_class(data=request.data)
        try:
            
            data.is_valid(raise_exception=True)
            ubicacion = data.validated_data.get('archivo')
            remove(settings.MEDIA_ROOT / ubicacion)
            return Response(data={
                   'message': 'Archivo eliminado exitosamente'
            })
            

        except Exception as e:
            return Response(data={
                'message': 'No se encontro el archivo a borrar',
                'content': e.args
            }, status=status.HTTP_404_NOT_FOUND)

































