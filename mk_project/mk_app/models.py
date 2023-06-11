from django.db import models

# Create your models here.
class set(models.Model):
    Name=models.CharField(max_length=20,default="")
    Age=models.IntegerField(default="")
