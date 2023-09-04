from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=250)
    priority = models.IntegerField()
    date = models.DateField(default='2023-08-04')

    def __str__(self) -> str:
        return self.name
