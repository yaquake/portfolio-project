# Generated by Django 2.1.3 on 2018-12-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180516_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=False, unique=True),
        ),
    ]
