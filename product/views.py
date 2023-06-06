from django.shortcuts import render
from rest_framework import status

from product.models import Product, Category
from product.serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class LatestProductList(APIView):
    """
    Create API view for latest products
    """

    def get(self, request, format=None):
        try:
            # Get latest five products
            products = Product.objects.all()[0:4]
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as exception:
            return Response({'error': str(exception)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
