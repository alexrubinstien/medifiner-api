# Generated by Django 2.0.9 on 2019-01-18 01:07

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0070_provider_related_county'),
    ]

    operations = [
        migrations.AddField(
            model_name='county',
            name='centroid',
            field=django.contrib.gis.db.models.fields.GeometryField(null=True, srid=4326, verbose_name='centroid'),
        ),
    ]
