from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from .models import Person,Reunion
from .serializers import PersonSerializer, PersonaSerializer2, PersonaSerializerPotente, ReunionSerializer, \
    ReunionSerializerSMF, ReunionSerializerLink


class ListaPersonas(ListView):
    template_name = "persona/personas.html"
    context_object_name = 'personas'
    queryset = Person.objects.all()


class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonListView(TemplateView):
    template_name = 'persona/lista.html'
    context_object_name = 'personas'


class PersonSearchApiView(ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def get_queryset(self):
        # filtro
        kword = self.kwargs['kword']
        return Person.objects.filter(full_name__icontains=kword)


class PersonCreateApiView(CreateAPIView):
    serializer_class = PersonSerializer


class PersonRetrieveApiView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonDestroyApiView(DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonUpdateApiView(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonAPILista(ListAPIView):
    """
        Vista para interactuar con serializadores
    """
    # serializer_class = PersonaSerializer
    serializer_class = PersonaSerializerPotente
    queryset = Person.objects.all()


class ReunionAPILista(ListAPIView):
    serializer_class = ReunionSerializer
    queryset = Reunion.objects.all()


class ReunionAPILista2(ListAPIView):
    serializer_class = ReunionSerializerSMF
    queryset = Reunion.objects.all()


class ReunionAPIListaLink(ListAPIView):
    serializer_class = ReunionSerializerLink
    queryset = Reunion.objects.all()