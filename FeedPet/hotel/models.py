from django.db import models
from master.models import Master
# Create your models here.
class Hotel(models.Model):

    hname = models.CharField(max_length=8)
    
    rank = models.CharField(max_length=2)
    
    full_name = models.CharField(max_length=12)
  
    incharge = models.CharField(max_length=3)

    phone = models.CharField(max_length=11)
    
    postalcode = models.CharField(max_length=5)
    
    district = models.CharField(max_length=3)
    
    address = models.CharField(max_length=25)
    
    def __str__(self):
     
        return self.hname
    
class Favor_hotel(models.Model):
    
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    
    def __str__(self):
     
        return self.hotel