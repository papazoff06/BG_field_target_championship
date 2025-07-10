from django.db import models

# Create your models here.

CHOICES = (
        ('4.5mm (.177)', '4.5mm (.177)'),
        ('5.5mm (.22)', '5.5mm (.22)'),
    )


class Rifle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    caliber = models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.caliber})"



class Pellets(models.Model):

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    weight_grains = models.IntegerField()
    caliber = models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.caliber})"


class Scope(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand} {self.model}"

