from django.db import models
from django.contrib.auth.models import User

from BG_field_target_championship.competition.models import Competition


# Create your models here.

class Registration(models.Model):
    shooter = models.ForeignKey(User, on_delete=models.CASCADE)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('shooter', 'competition')