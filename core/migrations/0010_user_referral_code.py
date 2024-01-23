# Generated by Django 4.2.5 on 2024-01-17 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_user_referral_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='referral_code',
            field=models.TextField(default='', max_length=6, unique=True),
            preserve_default=False,
        ),
    ]