# Generated by Django 4.2.5 on 2024-02-02 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0028_alter_product_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='productclass',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalogue.category'),
            preserve_default=False,
        ),
    ]
