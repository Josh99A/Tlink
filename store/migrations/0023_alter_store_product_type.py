# Generated by Django 4.2.5 on 2024-02-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_remove_store_type_store_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='product_type',
            field=models.CharField(choices=[('fashion', 'Fashion'), ('electronics', 'Electronics'), ('none', 'None')], default='none', help_text='The kind of products the store has', max_length=20),
        ),
    ]