# Generated by Django 5.0.6 on 2024-06-02 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_rename_categories_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]