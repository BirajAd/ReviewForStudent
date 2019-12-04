# Generated by Django 2.2.7 on 2019-12-02 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyDiary', '0006_auto_20191202_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
