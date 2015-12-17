from rest_framework import serializers
from patients.models import Person,Test,City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('url','id','city_name')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('test_name','glucose','hba1c','rbc','wbc','date')
 
class PersonSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    test_set = TestSerializer(many=True, required=False)
    class Meta:
        model = Person
        fields = ('url','id', 'title', 'name', 'address', 'city','test_set')


