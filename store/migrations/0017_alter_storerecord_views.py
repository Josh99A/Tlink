# Generated by Django 4.2.5 on 2024-02-19 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_comment_score_alter_storerecord_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storerecord',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
