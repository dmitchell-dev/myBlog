# Generated by Django 3.0.4 on 2020-05-04 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsblog', '0002_auto_20200504_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='preamble',
            field=models.TextField(blank=True),
        ),
    ]
