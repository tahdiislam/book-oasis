# Generated by Django 5.0.6 on 2024-06-01 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_book_categories_book_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='categories',
            new_name='category',
        ),
    ]
