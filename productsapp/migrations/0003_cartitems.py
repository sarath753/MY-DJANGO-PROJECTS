# Generated by Django 2.1.7 on 2024-07-16 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0002_products_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartitems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=40)),
                ('price', models.FloatField(null=True)),
                ('description', models.CharField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products_images/')),
            ],
        ),
    ]
