# Generated by Django 2.0.6 on 2018-06-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0010_auto_20180626_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemporaryFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
