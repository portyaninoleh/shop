from __future__ import unicode_literals

from django.views.generic import TemplateView

from common.utils import LoginRequiredMixin


class RegistrationLoginView(TemplateView):
    template_name = 'account/custom_registration.html'

    def get_context_data(self, **kwargs):
        context = super(RegistrationLoginView, self).get_context_data(**kwargs)
        return context

class UserSpaceView(LoginRequiredMixin, TemplateView):
    template_name = 'users/user-space.html'

user_space = UserSpaceView.as_view()
registration_login_view = RegistrationLoginView.as_view()