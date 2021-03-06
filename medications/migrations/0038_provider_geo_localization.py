# Generated by Django 2.0.6 on 2018-08-07 12:54

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0037_provider_relate_related_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='geo_localization',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326, verbose_name='localization'),
        ),
        migrations.AlterField(
            model_name='providermedicationthrough',
            name='supply',
            field=models.CharField(help_text='Use one of the following strings to add a valide supply: <24, 24, 24-48, >48', max_length=32, verbose_name='medication supply'),
        ),
    ]
