# Generated by Django 2.0.6 on 2018-07-25 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0024_county'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='state_us_id',
            field=models.PositiveIntegerField(null=True, unique=True, verbose_name='state us id'),
        ),
    ]