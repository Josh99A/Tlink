# Generated by Django 4.2.5 on 2024-01-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_rename_comments_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
