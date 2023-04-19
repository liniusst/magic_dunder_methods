# pylint: disable= missing-docstring
from dataclasses import dataclass
from typing import List


@dataclass
class Book:
    title: str
    author: str
    year: int
    isbn: int


@dataclass
class Library:
    books_list: List[Book] = []

    def add_book(self, new_book_list: List[Book]) -> None:
        for book in new_book_list:
            self.books_list.append(book)

    def find_book_by_isbn(self, isbn: int) -> Book:
        for book in self.books_list:
            if isbn == book.isbn:
                return book

    def remove_book(self, book_id: int) -> None:
        for book in self.books_list:
            if book_id == book.isbn:
                book_for_remove = self.find_book_by_isbn(book_id)
                self.books_list.remove(book_for_remove)

    def get_books_by_title(self, title: str) -> List[Book]:
        for book in self.books_list:
            if title == book.title:
                return book

    def get_books_by_author(self, author: str) -> List[Book]:
        for book in self.books_list:
            if author == book.author:
                return book

    def get_all_books(self) -> None:
        for book in self.books_list:
            print(
                f"Title: {book.title}, Author: {book.author}, published year: {book.year} and ISBN code: {book.isbn}"
            )


book_list = [
    Book(title="Užsimerk", author="Rachel Abbott", year=2023, isbn=9786094901904),
    Book(title="Viešnagė", author="Mark Edwards", year=2023, isbn=9786094901881),
    Book(title="Tobulas grobis", author="Helen Fields", year=2023, isbn=9786094901720),
    Book(title="Oliva Denaro", author="Viola Ardone", year=2023, isbn=9786090154489),
]

library = Library()
library.add_book(book_list)
library.remove_book(book_id=9786090154489)

print(library.get_books_by_title(title="Užsimerk"))
print(library.get_books_by_author(author="Helen Fields"))

library.get_all_books()
