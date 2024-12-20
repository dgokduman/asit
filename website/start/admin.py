# admin.py

from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'is_active', 'updated_at']
    list_filter = ['category', 'is_active']  # Kategoriye göre filtreleme

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)  # Kategori modelini admin paneline ekliyoruz
