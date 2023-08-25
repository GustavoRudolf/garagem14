from rest_framework.viewsets import ModelViewSet

from garagem.models import Acessorio,Categoria,Cor,Marca,Veiculo 
from garagem.serializers import AcessorioSerializer,CategoriaSerializer,CorSerializer,MarcaSerializer,VeiculoSerializer,VeiculoDetailSerializer,VeiculoListSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer