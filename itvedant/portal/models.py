from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dummy(models.Model):
    dname = models.CharField(max_length=30)
    demail=models.CharField(max_length=50)
    dcontact=models.IntegerField()