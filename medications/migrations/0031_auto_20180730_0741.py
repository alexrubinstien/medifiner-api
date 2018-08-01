# Generated by Django 2.0.6 on 2018-07-30 07:41

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0030_auto_20180730_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='county',
            name='geometry',
            field=django.contrib.gis.db.models.fields.GeometryField(null=True, srid=4326, verbose_name='geometry'),
        ),
        migrations.AddField(
            model_name='zipcode',
            name='geometry',
            field=django.contrib.gis.db.models.fields.GeometryField(null=True, srid=4326, verbose_name='geometry'),
        ),
    ]