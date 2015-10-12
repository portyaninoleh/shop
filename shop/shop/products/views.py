from __future__ import unicode_literals

from django.views.generic import ListView
from products.models import Products


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    model = Products

products_list = ProductsList.as_view()
