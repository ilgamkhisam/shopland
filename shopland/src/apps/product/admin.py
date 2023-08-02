from django.contrib import admin

# Register your models here.
from .models import Product, Category


class AdminSiteProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'image', 'link']
    list_filter = ['category']
    search_fields = ['name', 'price', 'link']



admin.site.register(Product,AdminSiteProduct)
admin.site.register(Category)