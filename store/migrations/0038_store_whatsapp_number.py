# Generated by Django 4.2.5 on 2024-03-22 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0037_comment_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='whatsApp_number',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]