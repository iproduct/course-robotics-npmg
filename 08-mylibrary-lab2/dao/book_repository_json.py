import json

from dao.book_repository import BookRepository
from model.book import Book

DEFAULT_BOOKS_DB_FILE = "books.json"
class BookRepositoryJson(BookRepository):
    def __init__(self, filename=DEFAULT_BOOKS_DB_FILE, id_generator = None):
        super().__init__(id_generator=id_generator)
        self.db_file_name = filename

    def save(self):
        save_to_file(self.db_file_name, self.find_all())

    def load(self):
        books_list = load_from_file(self.db_file_name, Book)
        self.delete_all()
        for book in books_list:
            self.insert(book)



# helper functions
def save_to_file(filename, entity_list):
    with open(filename, "wt") as f:
        return json.dump(entity_list, f, indent=4, default=dumper)

def dumper(entity):
    return entity.__dict__

def load_from_file(filename, entity_class):
    with open(filename, "rt") as f:
        return json.load(f, object_hook=obj_hook(entity_class))

def obj_hook(entity_class):
    def ob_hook(dict):
        obj = entity_class()
        obj.__dict__ = dict
        return obj
    return ob_hook


