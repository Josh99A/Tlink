# Generated by Django 4.2.5 on 2024-03-18 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0036_alter_comment_options_comment_delta_votes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='type',
            field=models.CharField(choices=[('PC', 'Parent Comment'), ('R', 'Reply')], default='PC', max_length=16),
        ),
    ]
