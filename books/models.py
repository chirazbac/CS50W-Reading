from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from django.utils import timezone

class User(AbstractUser):
    pass

class Book (models.Model):
    title = models.CharField(max_length = 64)
    author = models.CharField(max_length = 64)
    description = models.CharField(max_length = 256)
    coverUrl = models.CharField(max_length= 500, blank=True)
    numberPages = models.IntegerField(default =0)
    pages_per_day = models.IntegerField(default =0)
    pagesRead = models.IntegerField(default =0)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, related_name="user")

class Task (models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE, blank=True, related_name="book")
    date = models.DateField(default=date.today)
    status = models.CharField(
            max_length=20,
            choices=[('completed', 'Completed'), ('halfcompleted', 'Half Completed'), ('incompleted', 'Incompleted')],
            default='incompleted'
        )

    def serialize(self):
            return {
                "id": self.id,
                "title": self.book.title,
                "pages_per_day": self.book.pages_per_day,
                "pagesRead" : self.book.pagesRead,
                "status": self.status,
                "date": self.date.strftime("%b %d %Y, %I:%M %p"),

            }
class Notes (models.Model):
        book = models.ForeignKey(Book, on_delete = models.CASCADE, blank=True, null=True,  related_name="book_notes")
        task = models.ForeignKey(Task, on_delete = models.CASCADE, blank=True, related_name="task_notes")
        content = models.CharField(max_length = 256)
        favorite = models.BooleanField(default= False)
