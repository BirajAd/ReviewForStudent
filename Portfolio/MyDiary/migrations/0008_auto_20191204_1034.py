# Generated by Django 2.2.7 on 2019-12-04 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyDiary', '0007_auto_20191202_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='lat',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='lon',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='website',
            field=models.CharField(default='n/a', max_length=100),
            preserve_default=False,
        ),
    ]
