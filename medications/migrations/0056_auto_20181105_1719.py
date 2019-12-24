# Generated by Django 2.0.6 on 2018-11-05 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0055_auto_20181026_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providermedicationndcthrough',
            name='creation_date',
            field=models.DateTimeField(help_text='Creation date', verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='providermedicationndcthrough',
            name='last_modified',
            field=models.DateTimeField(help_text='Last modification date', verbose_name='last modified date'),
        ),
        migrations.AlterField(
            model_name='zipcode',
            name='counties',
            field=models.ManyToManyField(related_name='county_zipcodes', to='medications.County'),
        ),
        migrations.AddIndex(
            model_name='provider',
            index=models.Index(fields=['address', 'city', 'organization_id', 'phone', 'related_zipcode_id', 'state', 'store_number', 'zip'], name='medications_address_7f9d65_idx'),
        ),
        migrations.AddIndex(
            model_name='zipcode',
            index=models.Index(fields=['zipcode'], name='medications_zipcode_0fc7bd_idx'),
        ),
        migrations.AddIndex(
            model_name='zipcode',
            index=models.Index(fields=['state_id'], name='medications_state_i_6d1bab_idx'),
        ),
    ]
