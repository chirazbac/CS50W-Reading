# Generated by Django 4.2.10 on 2024-08-22 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='notes',
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=256)),
                ('favorite', models.BooleanField(default=False)),
                ('Task', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='books.task')),
            ],
        ),
    ]