# Generated by Django 3.2.5 on 2021-08-31 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reorev', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='passord',
            new_name='password',
        ),
    ]
