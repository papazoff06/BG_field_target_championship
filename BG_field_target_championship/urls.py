
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BG_field_target_championship.common.urls')),
    path('competition/', include('BG_field_target_championship.competition.urls')),
]
