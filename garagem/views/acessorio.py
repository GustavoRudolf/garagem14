from rest_framework.viewsets import ModelViewSet

from garagem.models import Acessorio,Categoria,Cor,Marca,Veiculo 
from garagem.serializers import AcessorioSerializer,CategoriaSerializer,CorSerializer,MarcaSerializer,VeiculoSerializer,VeiculoDetailSerializer,VeiculoListSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer