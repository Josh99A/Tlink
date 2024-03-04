# Generated by Django 4.2.5 on 2024-02-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_alter_storerecord_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='type',
            field=models.CharField(choices=[('fashion', 'Fashion'), ('electronics', 'Electronics'), ('all-in-one', 'All in One')], default='', max_length=20),
            preserve_default=False,
        ),
    ]
