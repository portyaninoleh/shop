from __future__ import unicode_literals

from allauth.account.forms import LoginForm

def extraContext(request):
    return {
        'login_form': LoginForm()
    }