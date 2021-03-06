# Generated by Django 2.0.6 on 2018-06-26 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0006_auto_20180626_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderMedicationThrough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supply', models.CharField(max_length=32, verbose_name='medication supply')),
                ('level', models.PositiveIntegerField(default=0, verbose_name='medication level')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_medication', to='medications.Medication')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provider_medication', to='medications.Provider')),
            ],
            options={
                'verbose_name': 'provider medication relation',
                'verbose_name_plural': 'provider medication relations',
            },
        ),
    ]
