# Generated by Django 2.0.6 on 2018-08-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Epidemic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False, help_text='Designates whether the flag Epidemic is active or not globally', verbose_name='active')),
            ],
            options={
                'verbose_name': 'Epidemic',
                'verbose_name_plural': 'Epidemic',
            },
        ),
    ]
