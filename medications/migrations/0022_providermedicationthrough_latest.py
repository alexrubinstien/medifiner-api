# Generated by Django 2.0.6 on 2018-07-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0021_auto_20180717_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='providermedicationthrough',
            name='latest',
            field=models.BooleanField(default=False, verbose_name='latest'),
        ),
    ]
