from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime, timedelta
from django.http import JsonResponse
from .models import User, Book, Task, Notes
import json
from django.utils import timezone
from django.utils.timezone import now
from django.utils.dateformat import format






from .models import User
# Create your views here.

def index(request):
    return render(request, "books/index.html")

def generate_reading_schedule(total_pages, pages_per_day):
    # Determine the number of days required to complete the book
    requiredDays = (total_pages + pages_per_day - 1) // pages_per_day

    # Start from today
    start_date = datetime.now().date()
    schedule = []

    for day in range(requiredDays):
        date = start_date + timedelta(days=day)
        schedule.append({
            'date': date,
            'pages_to_read': min(pages_per_day, total_pages - (day * pages_per_day))
        })

    return schedule
def addFavorite(request, id):
    note = Notes.objects.get(pk = id)
    taskId = note.task.id
    if request.method =="PUT":
        data = json.loads(request.body)
        note.favorite = data["favorite"]
        print(data["favorite"])
        note.save()
        return JsonResponse({"favorite": note.favorite, "taskId": taskId}, status=200)

def addBook(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        coverUrl = request.POST.get('imageUrl')
        number_pages = request.POST.get('numberPages')
        pages_per_day = request.POST.get('pages_per_day')
        if pages_per_day is None or number_pages is None:
          return HttpResponse("Please fill out all fields.", status=400)
        try:
            pages_per_day = int(pages_per_day)
            if pages_per_day <= 0:
                raise ValidationError("Pages per day must be a positive integer.")
        except ValueError:
            return HttpResponse("Invalid value for pages per day. Please enter a valid number.", status=400)

        # Ensure coverUrl has a default value if not provided
        if not coverUrl:
            coverUrl = "https://via.placeholder.com/150"
        Book.objects.create(
            title=title,
            author=author,
            description=description,
            coverUrl=coverUrl,
            numberPages=number_pages,
            pages_per_day=pages_per_day,
            user = request.user
        )

        return HttpResponseRedirect(reverse("bookList"))

def addNote(request):
     if request.method == "POST":
            data= json.loads(request.body)
            task_id = data.get("taskID")
            note = data.get("note")
            task = Task.objects.get(pk= task_id)
            newNote = Notes(task= task, content=note, book = task.book)
            newNote.save()
            return JsonResponse({"message": "Success", "note": note})

def removeNote(request, id):
        note = Notes.objects.get(pk = id)
        note.delete()
        return JsonResponse({"message": "Success", "id": note.task.id})

def removeBook(request, id):
    book = Book.objects.get(pk = id)
    book.delete()
    return JsonResponse({"message": "Success", "title": book.title})

def taskDetail(request, id):
            task= Task.objects.get(pk = id)
            formatted_date = format(task.date, 'l')
            if request.method == "GET":
                notes = task.task_notes.all().values('id', 'content', 'favorite')
                task_data = {
                        'id': task.id,
                        'title': task.book.title,
                        'pages_per_day': task.book.pages_per_day,
                        'notes': list(notes),
                        'date' : formatted_date
                    }
                return JsonResponse(task_data)
            elif request.method =="PUT":
                data = json.loads(request.body)
                task.status = data["status"]
                if data["status"] =="completed":
                   task.book.pagesRead = task.book.pagesRead+ task.book.pages_per_day
                elif data["status"] == "halfcompleted":
                     task.book.pagesRead =task.book.pagesRead+(task.book.pages_per_day/2)
                task.book.save()
                task.save()
                return HttpResponse(status=204)


def bookList(request):
      bookList = Book.objects.filter(user = request.user)
      book_data = []
      for book in bookList:
          percentage_read = (book.pagesRead / book.numberPages) * 100
          days_ago = (now().date() - book.created_at.date()).days
          favNotes = book.book_notes.filter(favorite=True).values('content')
          print(favNotes)
          book_data.append({
              'book': book,
              'percentage': percentage_read,
              'days_ago': days_ago,
              'favNotes' : favNotes
          })

      return render(request, 'books/bookList.html', {
           'books': book_data
          })


def bookDetail(request, id):
           book = Book.objects.get(pk = id)
           # Check if tasks already exist for this book
           tasks = Task.objects.filter(book=book).order_by('date')
           today = datetime.now().date()
           # If no tasks exist, generate the schedule and create tasks
           if not tasks.exists():
               schedule = generate_reading_schedule(book.numberPages, book.pages_per_day)
               tasks = []
               for item in schedule:
                   task = Task.objects.create(
                       book=book,
                       date=item['date'],
                   )
                   tasks.append(task)

           return render(request, 'books/bookDetailPage.html', {
               'tasks': tasks,
               'today': today,
               'book': book
           })





def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("bookList"))
        else:
            return render(request, "books/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "books/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "books/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "books/register.html", {
                "message": "Username already taken."
            })
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "books/register.html")
