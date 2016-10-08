from __future__ import unicode_literals
from django import template

register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})