# Generated by Django 2.0.6 on 2018-10-26 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0052_auto_20181003_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='user',
        ),
    ]