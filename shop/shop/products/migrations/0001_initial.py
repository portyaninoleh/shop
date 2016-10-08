# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=255, verbose_name='Category Name')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='products.Categories', null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=255, verbose_name='Image Name')),
                ('image', models.ImageField(default='', upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=255, verbose_name='Products')),
                ('description', models.TextField(default='', verbose_name='Description')),
                ('amount', models.IntegerField(default=0, verbose_name='Amount')),
                ('bought_by', models.IntegerField(default=0, verbose_name='Bought By')),
                ('price', models.FloatField(default=0.0, verbose_name='Price')),
                ('category', models.ManyToManyField(to='products.Categories', verbose_name='Categories')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=255, verbose_name='Video Name')),
                ('embed_code', models.CharField(default='', max_length=255, verbose_name='Embed Code')),
                ('product', models.ForeignKey(to='products.Products')),
            ],
        ),
        migrations.CreateModel(
            name='WareHouse',
            fields=[
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('number', models.IntegerField(verbose_name='Number')),
                ('site_key', models.IntegerField(serialize=False, verbose_name='Site key', primary_key=True)),
                ('city', models.CharField(max_length=255, verbose_name='City')),
            ],
            options={
                'verbose_name': 'WareHouse',
                'verbose_name_plural': 'WareHouses',
            },
        ),
        migrations.AddField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(to='products.Products'),
        ),
    ]
