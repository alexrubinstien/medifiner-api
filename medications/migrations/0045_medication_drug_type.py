# Generated by Django 2.0.6 on 2018-08-22 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0044_merge_20180821_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='drug_type',
            field=models.CharField(choices=[('b', 'Brand Drugs'), ('g', 'Generic Drugs'), ('p', 'Public Health Supply')], default='b', max_length=1, verbose_name='drug type'),
        ),
    ]
