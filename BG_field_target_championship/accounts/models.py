from django.contrib.auth.models import User
from django.db import models

from BG_field_target_championship.equipment.models import Scope, Rifle, Pellets


# Create your models here.
class ShooterProfile(models.Model):
    CHOICES = (
        ('Springer', 'Springer'),
        ('PCP overall', 'PCP overall'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    scope = models.ForeignKey(Scope, on_delete=models.SET_NULL, null=True, blank=True)
    rifle = models.ForeignKey(Rifle, on_delete=models.SET_NULL, null=True, blank=True)
    pellets = models.ForeignKey(Pellets, on_delete=models.SET_NULL, null=True, blank=True)
    shooting_class = models.CharField(max_length=50, choices=CHOICES)
    age = models.IntegerField(null=True, blank=True)
