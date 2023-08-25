from rest_framework.serializers import ModelSerializer

from garagem.models import Acessorio,Categoria,Cor,Marca,Veiculo

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = "__all__"