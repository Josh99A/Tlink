# Generated by Django 4.2.5 on 2024-02-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_store_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='prompted',
            field=models.BooleanField(default=False),
        ),
    ]
