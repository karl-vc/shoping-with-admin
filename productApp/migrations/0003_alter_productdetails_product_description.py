# Generated by Django 4.0.1 on 2022-01-28 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productApp', '0002_productimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='product_description',
            field=models.CharField(default='', max_length=2000),
        ),
    ]