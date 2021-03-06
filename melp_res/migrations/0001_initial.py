# Generated by Django 2.1.5 on 2019-01-24 19:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(0)])),
                ('name', models.CharField(max_length=80)),
                ('site', models.URLField(max_length=70)),
                ('email', models.EmailField(max_length=80)),
                ('phone', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=35)),
                ('state', models.CharField(max_length=35)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
    ]
