from django.db import models
from django.urls import reverse

# Create your models here.
class Sneaker(models.Model):
    # def __init__(self, name,brand,description,release):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=101)
    description = models.TextField(max_length=250)
    release = models.DateField('Release Date')
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sneaker_id': self.id})
        
