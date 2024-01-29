from rest_framework import viewsets
from .serializers import ReuniaoSerializer
from reunioes.models import Reuniao

class ReunioesViewSet(viewsets.ModelViewSet):
    queryset = Reuniao.objects.all()
    serializer_class = ReuniaoSerializer