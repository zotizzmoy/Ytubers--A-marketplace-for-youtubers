# Generated by Django 3.2.9 on 2021-11-15 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='healine',
            new_name='headline',
        ),
    ]
