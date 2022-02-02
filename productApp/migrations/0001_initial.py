# Generated by Django 4.0.1 on 2022-01-27 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=200)),
                ('product_price', models.CharField(default='', max_length=200)),
                ('product_description', models.CharField(default='', max_length=200)),
                ('product_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
