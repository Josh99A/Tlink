# Generated by Django 4.2.5 on 2024-05-16 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0039_remove_store_prompted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='whatsApp_number',
        ),
    ]