from django.db import models

rom django.utils import timezone

CONTINENTS = [
    ('Africa','Africa'),
    ('Europe','Europe'),
    ('Asia','Asia'),
]
# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'
