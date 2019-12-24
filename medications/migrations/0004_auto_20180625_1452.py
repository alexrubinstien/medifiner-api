# Generated by Django 2.0.6 on 2018-06-25 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0003_auto_20180625_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='longitude'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='operating_hours',
            field=models.CharField(blank=True, max_length=255, verbose_name='operating hours'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='start date'),
        ),
    ]
