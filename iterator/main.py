from abc import abstractmethod
from collections.abc import Iterator, Iterable
from typing import List


class Book:
    author: str
    title: str
    year: int

    def __init__(self, author: str, title: str, year: int):
        self.year = year
        self.title = title
        self.author = author

    def __repr__(self):
        return f'{self.title}: {self.author}, {self.year}'


class BaseCollection(Iterable):
    _books: List[Book]

    def __init__(self, books: List[Book] = []):
        self._books = books

    @abstractmethod
    def __iter__(self) -> Iterator:
        pass

    @abstractmethod
    def add_book(self, book: Book):
        pass


class CollectionIterator(Iterator):
    _position: int = None

    def __init__(self, collection: List[Book] = []):
        self._collection = collection
        self._position = 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return value


class TitleIterator(CollectionIterator):

    def __init__(self, collection: List[Book] = []):
        super().__init__(collection)
        self._collection = sorted(collection, key=lambda book: book.title)


class AuthorIterator(CollectionIterator):

    def __init__(self, collection: List[Book] = []):
        super().__init__(collection)
        self._collection = sorted(collection, key=lambda book: book.author)


class YearIterator(CollectionIterator):

    def __init__(self, collection: List[Book] = []):
        super().__init__(collection)
        self._collection = sorted(collection, key=lambda book: book.year)


class Collection(BaseCollection):

    def add_book(self, book: Book):
        self._books.append(book)

    def __iter__(self) -> CollectionIterator:
        """Iterate collection by default"""
        return CollectionIterator(self._books)

    def iterate_by_title(self) -> TitleIterator:
        """Iterate collection by title"""
        return TitleIterator(self._books)

    def iterate_by_author(self) -> AuthorIterator:
        """Iterate collection by author"""
        return AuthorIterator(self._books)

    def iterate_by_year(self) -> YearIterator:
        """Iterate collection by year"""
        return YearIterator(self._books)


if __name__ == '__main__':
    # Client's code:

    collection = Collection()

    for book in [
        Book('Leo Tolstoy', 'War and Peace', 1873),
        Book('Alexandre Dumas', 'Le Comte de Monte-Cristo', 1846),
        Book('Chuck Palahniuk', 'Fight Club', 1996),
    ]:
        collection.add_book(book)

    for book in collection:
        print(book)
    # War and Peace: Leo Tolstoy, 1873
    # Le Comte de Monte-Cristo: Alexandre Dumas, 1846
    # Fight Club: Chuck Palahniuk, 1996

    print('*'*50)

    for book in collection.iterate_by_title():
        print(book)
    # Fight Club: Chuck Palahniuk, 1996
    # Le Comte de Monte-Cristo: Alexandre Dumas, 1846
    # War and Peace: Leo Tolstoy, 1873

    print('*'*50)

    for book in collection.iterate_by_author():
        print(book)
    # Le Comte de Monte-Cristo: Alexandre Dumas, 1846
    # Fight Club: Chuck Palahniuk, 1996
    # War and Peace: Leo Tolstoy, 1873

    print('*'*50)

    for book in collection.iterate_by_year():
        print(book)
    # Le Comte de Monte-Cristo: Alexandre Dumas, 1846
    # War and Peace: Leo Tolstoy, 1873
    # Fight Club: Chuck Palahniuk, 1996
