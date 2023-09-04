from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    descri = models.TextField()

    def __str__(self) -> str:
        return self.name


class Team(models.Model):
    tname = models.CharField(max_length=250)
    timg = models.ImageField(upload_to='pics')
    tdescri = models.TextField()

    def __str__(self) -> str:
        return self.tname
