from django.db import models
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    image2 = models.FileField(blank=True, null = True)