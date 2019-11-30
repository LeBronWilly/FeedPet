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

    class Meta:
        verbose_name = '個人資料'
        verbose_name_plural = verbose_name
