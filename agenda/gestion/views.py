from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import PruebaSerializer, TareaSerializer, EtiquetaSerializer
from .models import Etiqueta, Tareas


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
    serializer_class = TareaSerializer
    
class EtiquetasApiView(ListCreateAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer















