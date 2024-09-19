document.addEventListener('DOMContentLoaded', function () {
    const gifs = [
        'https://media1.tenor.com/m/tNynT_eE9N4AAAAd/cloy-crash-landing-on-you.gif',
        'https://media1.tenor.com/m/oZyMJZnGyMwAAAAd/hyunbin-sonyejin-finger-heart.gif',
    ];

    function getCsrfToken() {
        const tokenElement = document.querySelector('meta[name="csrf-token"]');
        return tokenElement ? tokenElement.getAttribute('content') : '';
    }
    document.querySelectorAll('.DayItem').forEach(function (DayItem) {
        DayItem.addEventListener('click', function () {
            const taskId = this.dataset.taskId;
            taskDetails(taskId);
        });
    })

    function taskDetails(taskId) {
        fetch(`/tasks/${taskId}`)
            .then(response => response.json())
            .then(task => {
                console.log(task);
                const readingTask = document.getElementById('readingTask');
                if (readingTask) {
                    readingTask.innerHTML = `
                        <h2 class="TaskTitle">${task.title}</h2>
                        <p class="TaskPages">Pages to read ${task.date} : ${task.pages_per_day}</p>
                        <p class="TaskEstimatedTime">Always remember: 𝒯𝑜𝒹𝒶𝓎 𝒶 𝓇𝑒𝒶𝒹𝑒𝓇, 𝓉𝑜𝓂𝑜𝓇𝓇𝑜𝓌 𝒶 𝓁𝑒𝒶𝒹𝑒𝓇</p>
                        <div class="Buttons">
                            <button class="Button completed" id="completed-${taskId}">Mark as Completed</button>
                            <button class="Button halfCompleted" id="halfCompleted-${taskId}">Mark as Half Completed</button>
                            <button class="Button incompleted" id="incompleted-${taskId}">Mark as Incompleted</button>
                        </div>
                       `;
                }
                const noteSection = document.getElementById('notesSection');
                if (noteSection) {
                    noteSection.innerHTML = `
                        <div class="NotesSection">
                            <textarea class="NoteInput" placeholder="Add a note..."></textarea>
                            <button class="AddNoteButton">Add Note</button>
                            <ul class="NoteList"></ul>
                        </div>`;
                }

                const noteList = document.querySelector('.NoteList');
                if (noteList) {
                    noteList.innerHTML = '';
                    task.notes.forEach(note => {
                        const isFavorite = note.favorite ? 'fas' : 'far';
                        const newNote = document.createElement('li');
                        newNote.className = "NoteItem";
                        newNote.innerHTML = `
                            <span class="NoteText">${note.content}</span>
                            <div class="NoteButtons"  >
                                <button class="NoteButton deleteButton" data-note-id="${note.id}">
                                    <i class="fa fa-trash"></i>
                                </button>
                                <button class="NoteButton favoriteButton" 
                                 data-note-id="${note.id}">
                                    <i class="${isFavorite} fa-star" id="favorite-${note.id}"></i>
                                </button>
                            </div>`;
                        noteList.prepend(newNote);
                    });

                    const addNoteButton = document.querySelector('.AddNoteButton');
                    if (addNoteButton) {
                        addNoteButton.addEventListener('click', function () {
                            addNote(taskId);
                        });
                    }
                }

                document.querySelectorAll('.favoriteButton').forEach(function (favoriteButton) {
                    favoriteButton.addEventListener('click', function () {
                        const noteId = this.dataset.noteId;
                        if (noteId) {
                            favoriteNote(noteId);

                        }
                    });
                });

                document.querySelectorAll('.deleteButton').forEach(function (deleteButton) {
                    deleteButton.addEventListener('click', function () {
                        const noteId = this.dataset.noteId;
                        if (noteId) {
                            removeNote(noteId);

                        }
                    });
                });

                document.querySelector('.FlexContainer').style.display = 'flex';

                const completeButton = document.getElementById(`completed-${taskId}`);
                if (completeButton) {
                    completeButton.addEventListener('click', function () {
                        markAsComplete(taskId);
                    });
                }

                const halfCompleteButton = document.getElementById(`halfCompleted-${taskId}`);
                if (halfCompleteButton) {
                    halfCompleteButton.addEventListener('click', function () {
                        markAsHalfComplete(taskId);
                    });
                }


            });
    }

    function favoriteNote(noteId) {
        const starIcon = document.getElementById(`favorite-${noteId}`);
        const isFavorite = starIcon.classList.contains('fas');
        console.error(isFavorite);
        fetch(`/notes/${noteId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            },
            body: JSON.stringify({
                favorite : !isFavorite
            })
        })
            .then(response => {
                if (response.ok) {
                    // Toggle icon classes based on new favorite status
                    starIcon.classList.toggle('far', isFavorite);
                    starIcon.classList.toggle('fas', !isFavorite);
                }
    }
            )}

    function markAsComplete(taskId) {
        const randomGif = gifs[Math.floor(Math.random() * gifs.length)];
        const gifContainer = document.querySelector(".GifContainer");
        gifContainer.style.display = 'flex';
        document.getElementById("celebrationGif").src = randomGif;
        setTimeout(() => {
            gifContainer.style.display = 'none';
        }, 5000);
        fetch(`/tasks/${taskId}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCsrfToken()
                },
                body: JSON.stringify({
                    status: "completed"
                })
            })
                .then( () => {
                    const completeButton = document.getElementById(`completed-${taskId}`);
                    if (completeButton) {
                        completeButton.disabled = true;
                    }
                    const halfCompleted = document.getElementById(`halfCompleted-${taskId}`);
                    if (halfCompleted) {
                        halfCompleted.disabled = true;
                    }



                });
    }

    function markAsHalfComplete(taskId) {
        fetch(`/tasks/${taskId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            },
            body: JSON.stringify({
                status: "halfcompleted"
            })
        })
            .then( () => {
                const completeButton = document.getElementById(`completed-${taskId}`);
                if (completeButton) {
                    completeButton.disabled = true;
                }
                const halfCompleted = document.getElementById(`halfCompleted-${taskId}`);
                if (halfCompleted) {
                    halfCompleted.disabled = true;
                }



            });
    }


    function addNote(taskID) {
        const noteValue = document.querySelector('.NoteInput').value;
        if (noteValue.trim()) {
            fetch('/addNote', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCsrfToken()
                },
                body: JSON.stringify({
                    note: noteValue,
                    taskID: taskID
                })
            })
                .then(response => response.json())
                .then(result => {
                    document.querySelector('.NoteInput').value = '';
                    taskDetails(taskID)
                });
        }
    }

    function removeNote(noteId) {
            fetch(`/removeNote/${noteId}`)
                .then(response => response.json())
                .then(data => {
                    taskDetails(data.id)
                })

    }

});
