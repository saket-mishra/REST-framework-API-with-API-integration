from django.shortcuts import render
from patients.models import Person,Test,City
from patients.serializers import PersonSerializer,TestSerializer,CitySerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'cities': reverse('city-list', request=request, format=format)
    })



class CityDetail(generics.ListCreateAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        city = City.objects.get(pk=self.kwargs.get('pk', None))
        persons = Person.objects.filter(city=city)
        return persons


class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer

    def get_object(self):
        person_id = self.kwargs.get('pk', None)
        return Person.objects.get(pk=person_id)
