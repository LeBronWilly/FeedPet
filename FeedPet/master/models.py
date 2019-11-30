# master/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Master(AbstractUser):
    name = models.CharField(max_length=6)
    email = models.EmailField()
    GENDER = (('Male', '男'), ('Female', '女'))
    gender = models.CharField(max_length=6, choices=GENDER, null=True)

    def __str__(self):
        return self.username


class Pet(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    PETCLASS = (('Dog', '狗'), ('Cat', '貓'))
    petClass = models.CharField(max_length=3, choices=PETCLASS, null=True)
    petType = models.CharField(max_length=20)
    petName = models.CharField(max_length=20)
    birthday = models.DateField()
    weight = models.PositiveIntegerField()
    ligation = models.BooleanField()
    image = models.ImageField(upload_to='pets/')

    def __str__(self):
        return self.petName
