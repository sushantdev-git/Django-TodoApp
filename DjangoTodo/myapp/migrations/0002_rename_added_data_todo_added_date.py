# Generated by Django 3.2.7 on 2021-09-12 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='added_data',
            new_name='added_date',
        ),
    ]
