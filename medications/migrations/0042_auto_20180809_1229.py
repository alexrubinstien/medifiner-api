# Generated by Django 2.0.6 on 2018-08-09 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0041_auto_20180809_1225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='providercategory',
            options={'verbose_name': 'provider category', 'verbose_name_plural': 'provider categories'},
        ),
    ]