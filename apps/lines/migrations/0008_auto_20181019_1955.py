# Generated by Django 2.0.4 on 2018-10-19 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lines', '0007_auto_20181019_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linemodel',
            name='id',
            field=models.CharField(default='line_2018101919559a9c4aa76', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='id',
            field=models.CharField(default='route_2018101919559e1c1cfe9', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
