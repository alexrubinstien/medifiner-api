# Generated by Django 2.0.6 on 2018-07-18 13:02

from django.db import migrations, models
import localflavor.us.models
import medications.validators


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0022_providermedicationthrough_latest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='state',
        ),
        migrations.AddField(
            model_name='state',
            name='state_code',
            field=localflavor.us.models.USStateField(max_length=2, null=True, validators=[medications.validators.validate_state], verbose_name='us state code'),
        ),
        migrations.AddField(
            model_name='state',
            name='state_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='us state name'),
        ),
    ]
