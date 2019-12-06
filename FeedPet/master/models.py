# master/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class Master(AbstractUser):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    GENDER = (('Male', '男'), ('Female', '女'))
    gender = models.CharField(max_length=6, choices=GENDER, null=True)

    def __str__(self):
        return self.username


class Pet(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    petName = models.CharField(max_length=20)
    PETCLASS = (('Dog', '狗'), ('Cat', '貓'))
    petClass = models.CharField(max_length=3, choices=PETCLASS, null=True)
    petType = models.CharField(max_length=20)
    GENDER = (('Male', '公'), ('Female', '母'))
    petGender = models.CharField(max_length=6, choices=GENDER, null=True)
    birthday = models.DateField()
    weight = models.PositiveIntegerField()
    LIGATION = (('Yes', '有'), ('No', '無'))
    ligation = models.CharField(max_length=3, choices=LIGATION, null=True)
    image = models.ImageField(upload_to='pets/')

    def __str__(self):
        return self.petName
