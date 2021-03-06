# Generated by Django 4.0.1 on 2022-02-02 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productApp', '0007_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForgetPasswordModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('user_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UiidModel',
        ),
    ]
