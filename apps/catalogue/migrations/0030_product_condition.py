# Generated by Django 4.2.5 on 2024-03-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0029_productclass_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('N', 'New'), ('U', 'Used')], default='Used', max_length=4),
            preserve_default=False,
        ),
    ]
