# Generated by Django 2.2.7 on 2019-11-29 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyDiary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='distance',
            field=models.IntegerField(default=-999),
            preserve_default=False,
        ),
    ]