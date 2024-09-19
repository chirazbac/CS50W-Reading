# HarvardX CS50W: Web Programming with Python and JavaScript
## Introduction

The Book Reading Tracker is a dynamic web application designed to help users manage and monitor their reading progress. It offers an intuitive interface for tracking books, setting daily reading goals, and storing favorite notes.
## Why This Project?

The Book Reading Tracker project was designed to address a common challenge faced by  readers: staying consistent with reading goals. The application not only tracks progress but also provides motivation through personalized Gifs and note-taking feature with favorite marking, making the reading journey more enjoyable and rewarding. 
## Installation

1. Clone this repository.
2. In your terminal, cd into the Reading directory.
3. Run python manage.py makemigrations to make migrations for the books app.
4. Run python manage.py migrate to apply migrations to your database.
5. Run python manage.py runserver
   to  start the Django development server
  
   
## How the Book Reading Tracker Works

1. **Registration and Login**:
- New users must register and log in to access the app.
- Once logged in, users are presented with a list of books they are currently reading (if any exist)
2. **List books page**:  
-  After logging in, users are presented with a page that lists the books they are currently reading. Each book is displayed as a card with a progress bar showing the number of pages read out of the total.
-  Users can also displays their favorite notes for each book.
-  Users can delete books from their list.
 
3. **Adding a Book**:  
   Users can add a new book by clicking the "Add Book" button. A modal form appears, allowing them to enter details such as the book's title, author, description, image URL, number of pages, and the number of pages they plan to read each day.

4. **Book Details**:  
   Clicking on a book card takes the user to a detailed view of the book. This page displays the book's information, necessary days to complete it based on the user's reading speed, and a reading container where users can mark their progress (e.g., complete, half-complete). Additionally, users can add, delete, and favorite notes related to the book.

5. **Favorite Notes**:  
   Users can mark certain notes as favorites , which are then displayed by clicking in  "Favorites Notes" for each book  on the bookList page.

6. **Completion Celebration**:  
   Upon completing a task, users are greeted with a celebratory GIF, adding a personalized touch to the completion experience.

## Code and Organization

The application is organized into a Django project with the following structure:

- **`books/`**: The main Django application directory.
    - **`migrations/`**: Database migration files.
    - **`static/books/`**: Static assets such as JavaScript files, images, and CSS.
        - `book.js`: Handles dynamic interactions on book details page.
        - `bookList.js`: Manages the behavior of the book list view.
        - `bookLogo.png`: An image used as a logo/icon in the app.
        - `styles.css`: Custom CSS for styling the app's frontend.
    - **`templates/books/`**: HTML templates for rendering views.
        - `bookDetailPage.html`: Displays detailed information about a book and its related tasks.
        - `bookList.html`: Shows the list of books a user is reading.
        - `layout.html`: Base template used by other templates.
        - `login.html`: User login page.
        - `register.html`: User registration page.
    - `admin.py`: Configuration for Django's admin interface.
    - `apps.py`: Configuration file for the "books" app.
    - `models.py`: Defines the data models `Book`, `Note`and `Task`
    - `urls.py`: Maps URLs to views within the "books" app.
    - `views.py`: Handles the logic for processing requests and returning responses.
    
## Distinctiveness and Complexity

This project stands out due to its unique features and the complexity involved in its development. Unlike typical book management apps, this application integrates various functionalities that require seamless interaction between the frontend and backend. The project includes a dynamic progress tracking system, a note-taking feature with favorite marking, and personalized celebratory elements. Additionally, it ensures a mobile-responsive design, demonstrating an understanding of modern web development practices. The use of Django for backend management,  JavaScript for interactivity, and custom CSS for styling showcases the developer's ability to integrate multiple technologies to create a cohesive and engaging user experience.

