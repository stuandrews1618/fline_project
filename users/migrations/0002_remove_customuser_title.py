# Generated by Django 3.0.2 on 2020-01-18 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='title',
        ),
    ]