from django.db import models

# Create your models here.
class Food(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()


