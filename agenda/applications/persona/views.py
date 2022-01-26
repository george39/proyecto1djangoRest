from django.views.generic import ListView, TemplateView
from django.shortcuts import render

from .managers import ReunionManager

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    
)

from .models import Person, Reunion
from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    PersonSerializer2,
    PersonaSerializer3,
    ReunionSerializer,
    ReunionSerializer2,
    ReunionSerializerLink,
    PersonPagination,
    CountReunionSerializer
)
#from agenda.applications.persona import serializers
#from agenda.applications.persona import serializers





class ListaPersonas(ListView):
    template_name = "persona/persona.html"
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()



class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class PersonListView(TemplateView):
    template_name = 'persona/lista.html'


class PersonSearchApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )


class PersonCreateView(CreateAPIView):

    serializer_class = PersonSerializer


class PersonDetailView(RetrieveAPIView):

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


#Actualizar usuario
class PersonUpdateView(UpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


#Actualizar usuario pero trallendo los datos en el formulario
class PersonRetriveUpdateView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()    


# Vista para interactuar con serializadores
class PersonApiLista(ListAPIView):
    serializer_class = PersonaSerializer3

    def get_queryset(self):
        return Person.objects.all()


class ReunionApiList(ListAPIView):

    serializer_class = ReunionSerializer2

    def get_queryset(self):
        return Reunion.objects.all()        


# para pasar un link como parametro y no muchos datos
class ReunionApiListaLink(ListAPIView):

    serializer_class = ReunionSerializerLink

    def get_queryset(self):
        return Reunion.objects.all() 


# paginacion
class PersonPagination(ListAPIView):
    serializer_class = PersonSerializer
    pagination_class = PersonPagination

    def get_queryset(self):
        return Person.objects.all()


class ReunionByPersonJob(ListAPIView):
    serializer_class = CountReunionSerializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()