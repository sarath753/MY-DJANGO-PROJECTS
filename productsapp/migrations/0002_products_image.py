# Generated by Django 2.1.7 on 2024-07-16 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products_images/'),
        ),
    ]
