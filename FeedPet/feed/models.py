# feed/models.py
from datetime import date
from django.db import models
from master.models import Master, Pet


class Feed(models.Model):
    fname = models.CharField(max_length=20)
    fitem = models.CharField(max_length=10)
    fmat = models.CharField(max_length=500)
    fnut = models.CharField(max_length=100)
    fusage1 = models.CharField(max_length=50)
    fusage2 = models.CharField(max_length=50)
    fusage3 = models.CharField(max_length=50)
    flegalname = models.CharField(max_length=20)

    def __str__(self):
        return self.fname


class Record(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    water = models.PositiveIntegerField()
    amount = models.PositiveIntegerField()
    time = models.DateField(default=date.today)

    def __str__(self):
        return self.time

class Favor_feed(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
