# Generated by Django 4.2.10 on 2024-08-23 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_rename_pagenumber_book_numberpages'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]