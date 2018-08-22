# Generated by Django 2.0.6 on 2018-08-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_ex', '0004_user_permission_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='secret',
            field=models.CharField(max_length=20, unique=True, verbose_name='secret'),
            preserve_default=False,
        ),
    ]
