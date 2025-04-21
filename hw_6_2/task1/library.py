class Book:
    """
    Ініціалізація класу Book з використанням словника для зберігання інформації про книгу.

    OOP: Інкапсуляція — властивості книги приховані в екземплярі.
    SOLID: SRP — клас відповідає лише за дані книги.
    """
    def __init__(self, book_info: dict):
        self.author = book_info.get("author")
        self.title = book_info.get("title")
        self.publisher = book_info.get("publisher")
        self.genre = book_info.get("genre")
        self.year = book_info.get("year")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, Genre: {self.genre}, Year: {self.year}"

class Library:
    """
    Клас для керування домашньою бібліотекою.

    OOP: Інкапсуляція — управління доступом до колекції книг.
    SOLID: SRP — відповідає лише за роботу з колекцією Book.
    """
    def __init__(self):
        self.books = {}

    def add_book(self, book_number: int, book_info: dict):
        self.books[book_number] = Book(book_info)

    def search_books(self, **kwargs):
        return [book for book in self.books.values() if all(getattr(book, k) == v for k, v in kwargs.items())]

    def remove_book(self, book_number: int):
        if book_number in self.books:
            del self.books[book_number]

    def get_book(self, book_number: int):
        return self.books.get(book_number, "Книга не знайдена")

    def show_books(self):
        for book in self.books.values():
            print(book)

