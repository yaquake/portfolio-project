# Generated by Django 2.1.3 on 2018-12-18 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='short_description',
            field=models.TextField(default=None),
        ),
    ]