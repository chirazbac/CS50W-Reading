from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("bookDetail/<int:id>", views.bookDetail, name="bookDetail"),
    path("tasks/<int:id>", views.taskDetail, name="taskDetail"),
    path("addNote", views.addNote, name="addNote"),
    path("bookList", views.bookList, name="bookList"),
    path("addBook", views.addBook, name="addBook"),
    path("notes/<int:id>", views.addFavorite, name="addFavorite"),
    path("removeNote/<int:id>", views.removeNote, name="removeNote"),
    path("removeBook/<int:id>", views.removeBook, name="removeBook"),




]
