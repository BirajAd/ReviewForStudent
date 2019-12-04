# Generated by Django 2.2.7 on 2019-11-26 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=30)),
                ('checkId', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('reviewer', models.CharField(max_length=50)),
                ('businesses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_reviews', to='MyDiary.Business')),
            ],
        ),
    ]
