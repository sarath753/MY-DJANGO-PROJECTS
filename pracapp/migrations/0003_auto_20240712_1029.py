# Generated by Django 2.1.7 on 2024-07-12 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pracapp', '0002_contactenquiry_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactenquiry',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
