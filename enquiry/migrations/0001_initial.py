# Generated by Django 3.0.2 on 2020-01-18 23:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qfl_name', models.TextField(max_length=200, verbose_name='QFL Name')),
                ('qfl_address_1', models.TextField(blank=True, max_length=100)),
                ('qfl_address_2', models.TextField(blank=True, max_length=100)),
                ('qfl_town', models.TextField(blank=True, max_length=50)),
                ('qfl_postcode', models.TextField(max_length=10)),
                ('qfl_startdate', models.DateTimeField(default=datetime.datetime.now)),
                ('current_total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Price')),
                ('qfl_first_contact', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contact.Contact')),
            ],
        ),
    ]