# Generated by Django 5.0.6 on 2024-06-04 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='image',
        ),
    ]
