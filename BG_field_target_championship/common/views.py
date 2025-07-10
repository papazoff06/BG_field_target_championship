from django.contrib.auth import get_user_model
from django.contrib.auth.backends import UserModel
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import TemplateView


# Create your views here.
# def index(request):
#     return render(request, 'common/index.html')

class ShowHomePageView(TemplateView):
    template_name = 'common/index.html'
    user = get_user_model()