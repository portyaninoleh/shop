from __future__ import unicode_literals

from allauth.account import app_settings
from allauth.account.utils import complete_signup
from allauth.account.views import SignupView
from allauth.exceptions import ImmediateHttpResponse
from django.views.generic import TemplateView, View
from django.utils.translation import ugettext_lazy as _

from common.utils import LoginRequiredMixin, AjaxMixin, AjaxRequiredMixin
from products.models import WareHouse
from users.forms import RegistrationForm


class RegistrationLoginView(TemplateView):
    template_name = 'account/custom_registration.html'

    def get_context_data(self, **kwargs):
        context = super(RegistrationLoginView, self).get_context_data(**kwargs)
        context['form'] = RegistrationForm()
        return context


class CustomSignupView(SignupView):
    template_name = 'account/custom_registration.html'

    def get_form(self, form_class=None):
        form = super(CustomSignupView, self).get_form(form_class)
        form.fields['warehouses'].choices = WareHouse.objects.filter(city=self.request.POST.get('city'))\
            .values_list('site_key', 'description')
        return form




class GetWarehousesView(AjaxMixin, AjaxRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        city = request.GET.get('city')
        if not city:
            return self.render_to_response({'error': _('Empty City')})
        warehouses = WareHouse.objects.filter(city=city)
        return self.render_to_response([[{"SiteKey": wh.site_key,
                                         "DescriptionRu": wh.description} for wh in warehouses],])

class UserSpaceView(LoginRequiredMixin, TemplateView):
    template_name = 'users/user-space.html'

user_space = UserSpaceView.as_view()
registration_login_view = RegistrationLoginView.as_view()
custom_signup_view = CustomSignupView.as_view()
get_warehouses_view = GetWarehousesView.as_view()