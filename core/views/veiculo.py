from rest_framework.viewsets import ModelViewSet
from core.serializers import VeiculoSerializer
from core.models import Veiculo

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer