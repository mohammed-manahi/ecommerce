from rest_framework import serializers
from product.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    """
    Create product serializer
    """

    class Meta:
        model = Product
        # Define serializer fields for product endpoint
        fields = ['id', 'name', 'description', 'price', 'get_absolute_url', 'get_image', 'get_thumbnail']
