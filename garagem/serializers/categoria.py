from rest_framework.serializers import ModelSerializer

from garagem.models import Acessorio,Categoria,Cor,Marca,Veiculo

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"