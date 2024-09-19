document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.deleteBook').forEach(function (deleteBook) {
        deleteBook.addEventListener('click', function () {
            const bookId = this.dataset.bookId;
            if (bookId) {
                removeBook(bookId);

            }
        });
    });
    function removeBook(bookId) {
        fetch(`/removeBook/${bookId}`)
            .then(response => response.json())
            .then(data => {
                window.location.reload();            })

    }

});
