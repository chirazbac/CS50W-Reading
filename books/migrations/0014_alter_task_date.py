# Generated by Django 4.2.10 on 2024-08-25 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_alter_book_coverurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(verbose_name=models.DateField(default=datetime.date(2024, 8, 20))),
        ),
    ]
