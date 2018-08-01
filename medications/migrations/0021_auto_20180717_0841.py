# Generated by Django 2.0.6 on 2018-07-17 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0020_auto_20180717_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=18, max_digits=20, null=True, verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=18, max_digits=20, null=True, verbose_name='longitude'),
        ),
    ]