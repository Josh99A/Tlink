# Generated by Django 4.2.5 on 2024-03-02 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_userstorerecord_recently_viewd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstorerecord',
            old_name='recently_viewd',
            new_name='recently_viewed',
        ),
    ]
