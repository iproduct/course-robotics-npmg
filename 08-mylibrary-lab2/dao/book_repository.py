class BookRepository:
    def __init__(self, initial_books=[], id_generator=None):
        self.books = {}
        for book in initial_books:
            self.insert(book)
        self.id_generator = id_generator

    def insert(self, book):
        if (book.id is None or len(book.id.strip()) == 0) and self.id_generator is not None:
            book.id = next(self.id_generator)
        self.books[book.id] = book
        return book

    def update(self, book):
        self.books[book.id] = book
        return book

    def delete_by_id(self, book_id):
        removed = self.books[book_id]
        del self.books[book_id]
        return removed


    def delete_all(self):
        self.books = {}


    def count(self):
        return len(self.books)


    def find_all(self):
        return list(self.books.values())


    def find_by_id(self, book_id):
        return self.books[book_id]


    def find_by_predicate(self, filter_predicate):
        return filter(filter_predicate, self.find_all())
