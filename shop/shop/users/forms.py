from __future__ import unicode_literals

from allauth.socialaccount.forms import SignupForm
from django import forms
from django.contrib.auth.forms import (UserCreationForm,
                                       UserChangeForm)
from django.utils.translation import ugettext_lazy as _

from users.models import User

class CustomUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    class Meta:
        model = User
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    class Meta:
        model = User
        fields = '__all__'


class RegistrationForm(SignupForm):

    first_name = forms.CharField(label=_('First Name'), max_length=100)
    last_name = forms.CharField(label=_('Last Name'), max_length=100)
    city = forms.CharField(label=_('City'), max_length=100)
    phone =
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
