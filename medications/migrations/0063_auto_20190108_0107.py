# Generated by Django 2.0.9 on 2019-01-08 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0062_medicationdosage_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providermedicationndcthrough',
            name='level',
            field=models.IntegerField(default=0, verbose_name='medication level'),
        ),
    ]
