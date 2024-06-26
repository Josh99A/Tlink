# Generated by Django 4.2.5 on 2024-02-19 03:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0029_productclass_category'),
        ('store', '0013_store_prompted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='products',
        ),
        migrations.RemoveField(
            model_name='store',
            name='staff',
        ),
        migrations.CreateModel(
            name='StoreRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField()),
                ('followers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('products', models.ManyToManyField(blank=True, related_name='store', to='catalogue.product')),
                ('staff', models.ManyToManyField(related_name='stores', to=settings.AUTH_USER_MODEL)),
                ('store', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='record', to='store.store')),
            ],
        ),
    ]
