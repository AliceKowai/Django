from rest_framework import serializers
from pontos_turisticos.models import PontoTuristico

class PontoTuristicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = '__all__'