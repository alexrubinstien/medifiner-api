# Generated by Django 2.0.6 on 2018-07-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_ex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_test',
            field=models.BooleanField(default=False),
        ),
    ]
