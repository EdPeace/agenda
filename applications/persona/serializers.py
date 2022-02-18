from rest_framework import serializers

from .models import Person, Reunion, Hobby


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')


class PersonaSerializer2(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    # Extras
    active = serializers.BooleanField(required=False)


class PersonaSerializerPotente(serializers.ModelSerializer):
    active = serializers.BooleanField(required=False)

    class Meta:
        model = Person
        fields = ('__all__')

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('__all__')



class PersonaSerializerPlus(serializers.ModelSerializer):
    hobbies = HobbySerializer(many=True)
    class Meta:
        model = Person
        fields = ('__all__')


class ReunionSerializer(serializers.ModelSerializer):
    persona = PersonaSerializerPlus()

    class Meta:
        model = Reunion
        fields = ('__all__')



class ReunionSerializerSMF(serializers.ModelSerializer):
    fecha_hora = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = ('__all__')
    def get_fecha_hora(self,obj):
        return str(obj.fecha)+' - '+str(obj.hora)


class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )
        extra_kwargs={
            'persona': {'view_name':'persona app:detalle','lookup_field':'pk'}
        }
