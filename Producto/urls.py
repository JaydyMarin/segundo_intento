from rest_framework import routers
from .api import ProductoviewSet

router=routers.DefaultRouter()
router.register('api/Producto',ProductoviewSet,'Producto')

urlpatterns = router.urls 