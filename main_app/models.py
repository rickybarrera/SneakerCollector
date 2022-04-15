from django.db import models
from django.urls import reverse

# Create your models here.

CLEAN =(
    ('AM', 'Morning'),
    ('NOON', 'Mid day'),
    ('PM', 'Evening'),
    
)
class Lace(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('laces_detail', kwargs={'pk': self.id})

class Sneaker(models.Model):
    # def __init__(self, name,brand,description,release):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=101)
    description = models.TextField(max_length=250)
    release = models.DateField('Release Date')

    laces = models.ManyToManyField(Lace)
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'sneaker_id': self.id})

class Cleaning(models.Model):
    date = models.DateField()
    wash = models.CharField(
        max_length=4,
            choices=CLEAN,
            default=CLEAN[0][0]
    )
    sneaker = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
        
    def __str__(self):
        return f"{self.get_wash_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
