# Generated by Django 2.0.6 on 2018-07-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0012_auto_20180628_1254'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExistingMedication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='medication name')),
                ('ndc', models.CharField(max_length=32, unique=True, verbose_name='national drug code')),
                ('import_date', models.DateTimeField(auto_now_add=True, help_text='Date of import from the national database of this medication', verbose_name='import date')),
            ],
            options={
                'verbose_name': 'medication',
                'verbose_name_plural': 'medications',
            },
        ),
    ]
