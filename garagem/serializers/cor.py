from rest_framework.serializers import ModelSerializer

from garagem.models import Acessorio,Categoria,Cor,Marca,Veiculo

class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = "__all__"