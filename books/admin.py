from django.contrib import admin
from .models import User, Book, Task, Notes
# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Task)
admin.site.register(Notes)

