# Generated by Django 4.2.5 on 2024-03-02 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_userstorerecord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userstorerecord',
            old_name='data_viewed',
            new_name='date_viewed',
        ),
    ]
