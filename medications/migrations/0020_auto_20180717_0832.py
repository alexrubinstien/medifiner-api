# Generated by Django 2.0.6 on 2018-07-17 08:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models
import medications.validators


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0019_auto_20180712_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', localflavor.us.models.USStateField(max_length=2, validators=[medications.validators.validate_state], verbose_name='us state')),
                ('geometry', django.contrib.postgres.fields.jsonb.JSONField(default=dict, verbose_name='geometry')),
            ],
            options={
                'verbose_name': 'state',
                'verbose_name_plural': 'states',
            },
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', localflavor.us.models.USZipCodeField(max_length=10, validators=[medications.validators.validate_zip], verbose_name='zip code')),
                ('geometry', django.contrib.postgres.fields.jsonb.JSONField(default=dict, verbose_name='geometry')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zipcodes', to='medications.State')),
            ],
            options={
                'verbose_name': 'zip code',
                'verbose_name_plural': 'zip codes',
            },
        ),
        migrations.AddField(
            model_name='provider',
            name='related_zipcode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='providers', to='medications.ZipCode'),
        ),
    ]
