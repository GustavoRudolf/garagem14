from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from garagem.views import AcessorioViewSet,CategoriaViewSet,CorViewSet,MarcaViewSet,VeiculoViewSet
from usuario.router import router as usuario_router

router = DefaultRouter()

router.register(r"acessorios", AcessorioViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"cor", CorViewSet)
router.register(r"marca", MarcaViewSet)
router.register(r"veiculo", VeiculoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]

from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router

path("api/media/", include(uploader_router.urls)),

urlpatterns = [
    path("api/", include(usuario_router.urls)),
]