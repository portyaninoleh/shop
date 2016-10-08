from __future__ import unicode_literals

from mptt.models import MPTTModel
from mptt.models import TreeForeignKey

from django.utils.translation import ugettext_lazy as _
from django.db import models


class Categories(MPTTModel):
    name = models.CharField(_('Category Name'), max_length=255, default='')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __unicode__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(_('Products'), max_length=255, default='')
    description = models.TextField(_('Description'), default='')
    amount = models.IntegerField(_('Amount'), default=0)
    bought_by = models.IntegerField(_('Bought By'), default=0)
    price = models.FloatField(_('Price'), default=0.0)
    category = models.ManyToManyField(Categories, verbose_name=_('Categories'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductImages(models.Model):
    name = models.CharField(_('Image Name'), default='', max_length=255)
    image = models.ImageField(upload_to='product_images', default='')
    product = models.ForeignKey(Products)


class ProductVideo(models.Model):
    name = models.CharField(_('Video Name'), default='', max_length=255)
    embed_code = models.CharField(_('Embed Code'), default='', max_length=255)
    product = models.ForeignKey(Products)


class WareHouse(models.Model):
    description = models.CharField(_('Description'), max_length=255)
    phone = models.CharField(_('Phone'), max_length=20)
    number = models.IntegerField(_('Number'))
    site_key = models.IntegerField(_('Site key'), primary_key=True)
    city = models.CharField(_('City'), max_length=255)

    class Meta:
        verbose_name = _('WareHouse')
        verbose_name_plural = _('WareHouses')

    def __unicode__(self):
        return self.description