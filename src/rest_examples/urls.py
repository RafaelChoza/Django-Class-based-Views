
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import TestAPIView, TestViewset, ProductViewSet

from .views import ProductListViewPaginated 

router = DefaultRouter()
#router.register("test-viewset", TestViewset, basename="test-viewset")

router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    #path("api/test/", TestAPIView.as_view(), name="test-api-view"),
    path("product-list-paginated", ProductListViewPaginated.as_view()),
    #path('', include(router.urls)),  # Todas las rutas de tus ViewSets bajo /api/
    
]
