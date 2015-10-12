from django.contrib import admin

from products.models import Products
from products.models import Categories
from products.models import ProductImages
from products.models import ProductVideo


class ProductsImagesAdmin(admin.TabularInline):

    model = ProductImages


class ProductsVideoAdmin(admin.TabularInline):

    model = ProductVideo


class ProductsAdmin(admin.ModelAdmin):
    inlines = (ProductsImagesAdmin, ProductsVideoAdmin)

    class Meta:
        model = Products


admin.site.register(Products, ProductsAdmin)
admin.site.register(Categories)