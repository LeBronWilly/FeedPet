from django.db import models
from master.models import Master
# from django.contrib.gis.db import models as geomodels

# Create your models here.
class Hotel(models.Model):

    hname = models.CharField(max_length=20)
    
    rank = models.CharField(max_length=20)
    
    full_name = models.CharField(max_length=30)
  
    incharge = models.CharField(max_length=30)

    phone = models.CharField(max_length=30)
    
    postalcode = models.CharField(max_length=30)
    
    district = models.CharField(max_length=30)
    
    address = models.CharField(max_length=40)
    
    # name = models.CharField(max_length=100, blank=False)

    # geometry = geomodels.PointField()

    def __str__(self):
     
        return self.hname
    
class Favor_hotel(models.Model):
    
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    
    def __str__(self):
     
        return self.hotel