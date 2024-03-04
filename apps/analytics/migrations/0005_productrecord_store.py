# Generated by Django 4.2.5 on 2024-02-29 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_comment_parent_comment'),
        ('analytics', '0004_productrecord_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productrecord',
            name='store',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.store'),
        ),
    ]
