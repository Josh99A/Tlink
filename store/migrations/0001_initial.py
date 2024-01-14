# Generated by Django 4.2.5 on 2024-01-13 13:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogue', '0028_alter_product_seller'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('location', models.CharField(choices=[('BW', 'Bweyale'), ('KY', 'Kyradongo')], max_length=20)),
                ('primary_image', models.ImageField(upload_to='store')),
                ('location_image1', models.ImageField(upload_to='location')),
                ('location_image2', models.ImageField(blank=True, null=True, upload_to='location')),
                ('location_image3', models.ImageField(blank=True, null=True, upload_to='location')),
                ('location_image4', models.ImageField(blank=True, null=True, upload_to='location')),
                ('products', models.ManyToManyField(related_name='store', to='catalogue.product')),
                ('staff', models.ManyToManyField(related_name='stores', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
