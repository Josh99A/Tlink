# Generated by Django 4.2.5 on 2024-03-12 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0034_remove_storerecord_followers_followinfo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followinfo',
            old_name='data_followed',
            new_name='date_followed',
        ),
    ]
