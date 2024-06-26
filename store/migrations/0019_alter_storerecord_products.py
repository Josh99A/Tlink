# Generated by Django 4.2.5 on 2024-02-29 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0029_productclass_category'),
        ('store', '0018_comment_parent_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storerecord',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='store_record', to='catalogue.product'),
        ),
    ]
