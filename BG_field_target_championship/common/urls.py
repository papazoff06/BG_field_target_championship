from django.urls import path

from BG_field_target_championship.common import views

urlpatterns = [
    path('', views.ShowHomePageView.as_view(), name='index'),
]