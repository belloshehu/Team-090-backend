from django.db import models

rom django.utils import timezone

CONTINENTS = [
    ('Africa','Africa'),
    ('Europe','Europe'),
    ('Asia','Asia'),
]
# Create your models here.
class Service(models.Model):
    """ Model for services rendered"""
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}'

class Category(models.Model):
    """ Model for service categories"""
    name = models.CharField(max_length=100)
    services = models.ForeignKey(Service, on_delete=models.CASCADE)
    document_required = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

class Country(models.Model):
    """ Model for supported countries"""
    name = models.CharField(max_length=50)
    continent = models.CharField(choices=CONTINENTS, max_length=50)

    def __str__(self):
        return f'{self.name}'
