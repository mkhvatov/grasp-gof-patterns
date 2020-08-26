from abc import ABC, abstractmethod
from collections.abc import Iterator, Iterable
from typing import List, Optional


class Book:
    author: str
    title: str
    year: int

    def __init__(self, author: str, title: str, year: int):
        self.year = year
        self.title = title
        self.author = author


class BaseCollection(Iterable):
    _books: List[Book]

    def __init__(self, books: Optional[List[Book]] = None):
        if not books:
            books = list()
        self._books = books

    @abstractmethod
    def __iter__(self) -> Iterator:
        pass

    @abstractmethod
    def add_book(self, book: Book):
        pass


class Collection(BaseCollection):

    def add_book(self, book: Book):
        self._books.append(book)


class CollectionIterator(Iterator):
    pass


if __name__ == '__main__':
    # Client's code:

    collection = Collection()

    for book in [
        Book('Leo Tolstoy', 'War and Peace', 1873),
        Book('Alexandre Dumas', 'Le Comte de Monte-Cristo', 1846),
        Book('Chuck Palahniuk', 'Fight Club', 1996),
    ]:
        collection.add_book(book)

    # for book in collection._books:
    #     print(book.author, book.year)
