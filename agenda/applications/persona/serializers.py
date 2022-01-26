from dataclasses import fields
#from typing_extensions import Required
from .models import Person, Reunion, Hobby
from rest_framework import serializers, pagination


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone'
        )


# serializar que no esta cargando un modelo 
class PersonaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    # para agregar atributos que no estan en el modelo
    activo = serializers.BooleanField(required=False)


class PersonSerializer2(serializers.ModelSerializer):
    activo = serializers.BooleanField(default=False)
    class Meta:
        model = Person
        fields = ('__all__')


# para un foreyngkey
class ReunionSerializer(serializers.ModelSerializer):

    persona = PersonSerializer()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona'
        )


# para un many to many
class HobbySerializer(serializers.ModelSerializer):

    class Meta:
        model = Hobby 
        fields = ('__all__')


class PersonaSerializer3(serializers.ModelSerializer):

    hobbies = HobbySerializer(many=True) 

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created'
        )              



class ReunionSerializer2(serializers.ModelSerializer):
    fecha_hora = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            'fecha_hora'
        )

    def get_fecha_hora(self, obj):
        return str(obj.fecha) + ' - ' + str(obj.hora)        


# para pasar un link como parametro y no muchos datos
class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona'
        )
        extra_kwargs = {
            'persona': {'view_name': 'persona_app:detalle', 'lookup_field': 'pk'}
        }


class PersonPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100


class CountReunionSerializer(serializers.Serializer):
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()