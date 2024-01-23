# Generated by Django 4.2.5 on 2024-01-17 15:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_user_gender_user_loation_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='referral_code',
            field=models.IntegerField(default=2, max_length=6, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='referral_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='referrals',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
