from __future__ import unicode_literals

from allauth.socialaccount.forms import SignupForm
from django import forms
from django.contrib.auth.forms import (UserCreationForm,
                                       UserChangeForm)
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.validators import validate_international_phonenumber

from products.models import WareHouse
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


class RegistrationForm(forms.Form):

    email = forms.EmailField(widget=forms.TextInput(attrs={'type': 'email'}))
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Confirm Password'), widget=forms.PasswordInput)
    first_name = forms.CharField(label=_('First Name'), max_length=100)
    last_name = forms.CharField(label=_('Last Name'), max_length=100)
    phone = forms.CharField(label=_('Phone'), validators=[validate_international_phonenumber])
    city = forms.CharField(label=_('City'), max_length=100)
    warehouses = forms.MultipleChoiceField(label=_('Warehouses'), choices=())

    def save(self, request):
        user = User(
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            city=self.cleaned_data['city']
        )
        user.phone = self.cleaned_data['phone']
        user.set_password(self.cleaned_data['password1'])
        user.save()
        user.ware_houses.add(*[i for i in WareHouse.objects.filter(site_key__in=self.cleaned_data['warehouses'])])
        return user

    def clean_email(self):
        try:
            User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        else:
            raise forms.ValidationError(_('Such email already registered'))

    def clean(self):
        if self.cleaned_data.get('password1') and self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError(_('Passwords did not match'))
        return self.cleaned_data

    def clean_password1(self):
        if len(self.cleaned_data['password1']) < 6:
            raise forms.ValidationError(_('Password must contain at least 6 characters'))
        return self.cleaned_data['password1']