from __future__ import unicode_literals

import random, decimal
import factory

from django.utils import lorem_ipsum

from products.models import (Categories,
                             Products,
                             ProductImages)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categories

    @factory.lazy_attribute
    def name(self):
        return lorem_ipsum.words(1, False)

    parent = None


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Products

    @factory.lazy_attribute
    def name(self):
        return lorem_ipsum.words(2, False)

    @factory.lazy_attribute
    def description(self):
        return lorem_ipsum.words(5, False)

    @factory.lazy_attribute
    def amount(self):
        return random.randint(0, 100)

    @factory.lazy_attribute
    def bought_by(self):
        return random.randint(0, 100)

    @factory.lazy_attribute
    def price(self):
        return float(decimal.Decimal(random.random() * 100).quantize(decimal.Decimal('.01')))

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for pr in extracted:
                self.category.add(pr)
