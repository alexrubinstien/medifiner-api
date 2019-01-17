# Generated by Django 2.0.9 on 2019-01-17 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0067_medication_dosage'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='related_state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='providers', to='medications.State'),
        ),
    ]
