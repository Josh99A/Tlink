# Generated by Django 4.2.5 on 2024-01-17 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_user_referral_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='referral_code',
        ),
    ]
