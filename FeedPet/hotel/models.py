from django.db import models

# Create your models here.
class Hotel(models.Model):
    
    sequence = models.CharField(max_length=15)
    
    year_eva = models.CharField(max_length=8)
    
    name = models.CharField(max_length=20)
    
    postalcode = models.CharField(max_length=5)
    
    area = models.CharField(max_length=3)
    
    address = models.CharField(max_length=25)
    
    def __str__(self):
     
        return self.name
    