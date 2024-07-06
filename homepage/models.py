from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Coustomer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    nickname=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    ph=models.IntegerField(default=True)
    zipcode=models.IntegerField()
    def __str__(self):
        return str(self.nickname)