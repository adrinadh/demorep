from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    descri = models.TextField()

    def __str__(self) -> str:
        return self.name
