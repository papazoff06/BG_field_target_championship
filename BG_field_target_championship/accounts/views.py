from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from BG_field_target_championship.accounts.forms import ShooterRegisterForm


# Create your views here.
class ShooterRegisterView(CreateView):
    model = get_user_model()
    form_class = ShooterRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        login(self.request, user)
        return response