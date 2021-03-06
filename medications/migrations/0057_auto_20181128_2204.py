# Generated by Django 2.0.6 on 2018-11-28 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0056_auto_20181105_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='county',
            name='active_provider_count',
            field=models.PositiveIntegerField(null=True, verbose_name='active provider count'),
        ),
        migrations.AddField(
            model_name='county',
            name='total_provider_count',
            field=models.PositiveIntegerField(null=True, verbose_name='active provider count'),
        ),
        migrations.AddField(
            model_name='state',
            name='active_provider_count',
            field=models.PositiveIntegerField(null=True, verbose_name='active provider count'),
        ),
        migrations.AddField(
            model_name='state',
            name='total_provider_count',
            field=models.PositiveIntegerField(null=True, verbose_name='active provider count'),
        ),
        migrations.AddField(
            model_name='zipcode',
            name='active_provider_count',
            field=models.PositiveIntegerField(null=True, verbose_name='active provider count'),
        ),
        migrations.AddField(
            model_name='zipcode',
            name='total_provider_count',
            field=models.PositiveIntegerField(null=True, verbose_name='active provider count'),
        ),
    ]
