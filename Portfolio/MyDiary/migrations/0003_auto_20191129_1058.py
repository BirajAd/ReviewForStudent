# Generated by Django 2.2.7 on 2019-11-29 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyDiary', '0002_business_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='distance',
            field=models.IntegerField(default=-999),
        ),
    ]
