# Generated by Django 2.2.7 on 2019-11-07 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='slug',
            field=models.SlugField(default='null', unique=True),
        ),
    ]
