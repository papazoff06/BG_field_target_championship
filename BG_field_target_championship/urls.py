
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipment/', include('BG_field_target_championship.equipment.urls')),
    path('competition/', include('BG_field_target_championship.competition.urls')),
    path('', include('BG_field_target_championship.common.urls')),
    path('hotels/', include('BG_field_target_championship.hotels.urls')),
]
