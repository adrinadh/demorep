# Generated by Django 4.2.4 on 2023-09-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=250)),
                ('task_desc', models.CharField(max_length=250)),
                ('date_created', models.DateField(auto_now=True)),
            ],
        ),
    ]