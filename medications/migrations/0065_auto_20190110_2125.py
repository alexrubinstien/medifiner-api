# Generated by Django 2.0.9 on 2019-01-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0064_auto_20190109_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providermedicationndcthrough',
            name='creation_date',
            field=models.DateTimeField(db_index=True, help_text='Creation date', verbose_name='creation date'),
        ),
    ]