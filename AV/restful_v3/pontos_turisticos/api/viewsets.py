from rest_framework import viewsets
from .serializers import PontoTuristicosSerializer
from pontos_turisticos.models import PontoTuristico

class PontosTuristicosViewSet(viewsets.ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicosSerializer