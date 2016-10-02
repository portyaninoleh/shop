from __future__ import unicode_literals

from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('users.views',
    url(r'^register_login/$', 'registration_login_view', name='registration_login'),
    url(r'', 'user_space', name='space'),
)
