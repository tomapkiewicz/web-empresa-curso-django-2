# Generated by Django 3.1.7 on 2021-04-03 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20210401_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='./servicios', verbose_name='imagen'),
        ),
    ]
