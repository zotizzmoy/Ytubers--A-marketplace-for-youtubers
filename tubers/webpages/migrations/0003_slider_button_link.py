# Generated by Django 3.2.9 on 2021-11-20 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_rename_healine_slider_headline'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_link',
            field=models.URLField(null=True),
        ),
    ]
