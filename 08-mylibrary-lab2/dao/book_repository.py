
class BookRepository:
    def __init__(self, initial_books=[], id_generator = None):
        self.books = {}
        for book in initial_books:
            self.insert(book)
        self.id_generator = id_generator

    def insert(self, book):
        if(len(book.id.strip()) == 0 and self.id_generator is not None):
            book.id = next(self.id_generator)
        self.books[book.id] = book