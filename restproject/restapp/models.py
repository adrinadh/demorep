from django.db import models

# Create your models here.


class task(models.Model):
    task_name = models.CharField(max_length=250)
    task_desc = models.CharField(max_length=250)
    date_created = models.DateField(auto_now=True)
    completed = models.BooleanField(default=False)
    image = models.ImageField(
        upload_to='images', default='image/None/Noimg.jpg')
