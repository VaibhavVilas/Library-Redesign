from models import Book
from storage import Storage

# template of BookManager to manage books


class BookManager:

    # defining attributes for books.json file where books will be stored
    def __init__(self, file_path='books.json'):
        self.file_path = file_path
        self.books = self.load_books()

    # method to load/read books from books.json
    def load_books(self):
        books_data = Storage.load_data(self.file_path)
        # converts JSON data to Book object
        return [Book(**book) for book in books_data]

    # method to save books in books.json
    def save_books(self):
        books_data = [book.__dict__ for book in self.books]
        Storage.save_data(self.file_path, books_data)

    # method to check whether a book is available or not.
    def is_book_available(self, isbn):
        # since isbn is unique for every book we base our check on that
        return any(book.isbn == isbn for book in self.books)

    # method to add a book
    def add_book(self, title, author, isbn):

        # check if the given book already exists
        if self.is_book_available(isbn):
            print('\nBook already exists in the library!')
            return

        # appending the given book and saving it in books.json
        book = Book(title, author, isbn)
        self.books.append(book)
        self.save_books()
        print('\nBook Added')

    # method to display list of books
    def list_books(self):
        # to check if the list is empty
        if not self.books:
            print('\nLibrary has no books!!')
        else:
            for book in self.books:
                print('\n', book)
