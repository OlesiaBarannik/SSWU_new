class Book:
    def __init__(self, book_info: dict):
        """
        Ініціалізація класу Book з використанням словника для зберігання інформації про книгу.
        """
        self.author = book_info.get("author")
        self.title = book_info.get("title")
        self.publisher = book_info.get("publisher")
        self.genre = book_info.get("genre")
        self.year = book_info.get("year")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}, Genre: {self.genre}, Year: {self.year}"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_number: int, book_info: dict):
        """
        Додає книгу в бібліотеку.
        """
        book = Book(book_info)
        self.books[book_number] = book

    def search_books(self, **kwargs):
        """
        Шукає книги за переданими параметрами (наприклад, за автором, роком, жанром).
        """
        found_books = []
        for book in self.books.values():
            if all(getattr(book, key) == value for key, value in kwargs.items()):
                found_books.append(book)
        return found_books

    def remove_book(self, book_number: int):
        """
        Видаляє книгу з бібліотеки за її порядковим номером.
        """
        if book_number in self.books:
            del self.books[book_number]

    def get_book(self, book_number: int):
        """
        Повертає книгу за її порядковим номером.
        """
        return self.books.get(book_number, "Книга не знайдена")

    def show_books(self):
        """
        Виводить всі книги в бібліотеці.
        """
        for book in self.books.values():
            print(book)


