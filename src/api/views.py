from rest_framework import views
from rest_framework.response import Response
from .models import Product
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

class ProductAPIView(views.APIView):
    
    def get(self, request):
        products = Product.objects.all()
        product_data = [{"id": product.id, "title": product.title, "description": product.description, "price": str(product.price)} for product in products]
        return JsonResponse(product_data, safe=False)

    def post(self, request):
        data = request.data
        title = data.get("title")
        description = data.get("description")
        price = data.get("price")

        if not title or not description or not price:
            return Response({"error": "Todos los campos son obligatorios."}, status=400)

        product = Product.objects.create(title=title, description=description, price=price)
        return Response({"id": product.id, "message": "Producto creado con éxito"}, status=201)

    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        data = request.data
        
        product.title = data.get("title", product.title)
        product.description = data.get("description", product.description)
        product.price = data.get("price", product.price)
        
        product.save()
        return Response({"message": "Producto actualizado con éxito"})

    def patch(self, request, pk):
        return self.put(request, pk)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({"message": "Producto eliminado"})
