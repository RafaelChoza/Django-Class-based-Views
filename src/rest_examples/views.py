from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404

from .serializers import TestSerializer, ProductSerializer
from .models import Product

class TestAPIView(APIView):
    """APIView de Prueba"""
    serializer_class = TestSerializer

    def get(self, request, format=None):
        """Regresa una lista de caracteristicas de un APIView"""
        apiview_info = [
            "Usa métodos HTTP como funciones (get, post, put, patch, delete)",
            "Es similar a un Django View tradicional",
            "Te da el mayor control de la lógica de la app",
            "Es mapeado manualmente a las urls",
        ]

        return Response({"message": "hola", "apiview_info": apiview_info})
    
    def post(self, request):
        """Crea un mensaje con el nombre ingresado"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"hola {name}!"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        """Manejar la actualización de un objeto"""
        return Response({"method":"PUT"})
    
    def patch(self, request, pk=None):
        """Manejar la actualización parcial de un objeto"""
        return Response({"method":"PATCH"})
    
    def delete(self, request, pk=None):
        """Manejar la eliminación de un objeto"""
        return Response({"method":"DELETE"})
    
class TestViewset(ViewSet):
    """Test API Viewset"""

    serializer_class = TestSerializer

    def list(self, request):
        """Regresa un listado de caracteristicas de los Viewsets"""
        viewset_info = [
            "Usa acciones (list, create, retrieve, update, partial_update, destroy)",
            "Se mapea automaticamente a los urls usando routers",
            "Provee mas funcionalidad con menos codigo"
        ]
        return Response({"message": "Hola", "viewset_info": viewset_info})
    
    def create(self, request):
        """Crea un mensaje de saludo"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"hola {name}!"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        """Maneja la consulta de un objeto por su ID"""
        return Response({"method": "GET"})
    
    def update(self, request, pk=None):
        """Maneja la actualización de un objeto por su ID"""
        return Response({"method": "PUT"})
    
    def partial_update(self, request, pk=None):
        """Maneja la actualización parcial de un objeto por su ID"""
        return Response({"method": "PATCH"})
    
    def destroy(self, request, pk=None):
        """Maneja la eliminación de un objeto por su ID"""
        return Response({"method": "DELETE"})
    
class ProductViewSet(ViewSet):

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)