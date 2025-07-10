from django.db import models

from BG_field_target_championship.hotels.models import Hotel


# Create your models here.
class Competition(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    duration = models.IntegerField()
    location = models.CharField(max_length=200)
    hotels = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True)
    is_open = models.BooleanField(default=True)  # Can register or not
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.date}"