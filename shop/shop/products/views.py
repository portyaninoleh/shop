from __future__ import unicode_literals

from django.views.generic import ListView, TemplateView
from products.models import Products


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    model = Products


class HomeView(TemplateView):
    template_name = "products/home.html"


products_list = ProductsList.as_view()
home = HomeView.as_view()