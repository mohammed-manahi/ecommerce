from django.contrib import admin
from product.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Register product model in admin site
    """
    list_display = ['id', 'name', 'slug', 'description', 'price']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Register category model in admin site
    """
    list_display = ['name', 'slug']
