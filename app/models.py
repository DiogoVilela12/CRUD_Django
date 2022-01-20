from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    score = models.IntegerField()

