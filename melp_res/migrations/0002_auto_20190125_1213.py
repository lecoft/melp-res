# Generated by Django 2.1.5 on 2019-01-25 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melp_res', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurants',
            options={'verbose_name': 'Restaurant', 'verbose_name_plural': 'Restaurants'},
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='restaurants',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
