from dao.book_repository import BookRepository
from dao.book_repository_json import BookRepositoryJson
from model.book import Book
from util.uuid_sequence_generator import uuid_sequence_genrator

if __name__ == '__main__':
    b1 = Book(None, "Head First Python", "A Brain Friendly Guide", ["Paul Barry"], "1491919531",
              "O'Reilly UK Ltd.", 2016, 41.82, "Software Engineering",
              ["python", "introduction", "programming", "examples"],
              "Want to learn the Python language without slogging your way through how-to manuals? With Head First Python, you&;ll quickly grasp Python&;s fundamentals, working with the built-in data structures and functions. Then you&;ll move on to building your very own webapp, exploring database management, exception handling, and data wrangling. If you&;re intrigued by what you can do with context managers, decorators, comprehensions, and generators, it&;s all here. This second edition is a complete learning experience that will help you become a bonafide Python programmer in no time."
              )
    b2 = Book(None, "Introduction Python", "A Brain Friendly Guide", ["Paul Barry"], "1491919531",
              "O'Reilly UK Ltd.", 2016, 41.82, "Software Engineering",
              ["python", "introduction", "programming", "examples"],
              "Want to learn the Python language without slogging your way through how-to manuals? With Head First Python, you&;ll quickly grasp Python&;s fundamentals, working with the built-in data structures and functions. Then you&;ll move on to building your very own webapp, exploring database management, exception handling, and data wrangling. If you&;re intrigued by what you can do with context managers, decorators, comprehensions, and generators, it&;s all here. This second edition is a complete learning experience that will help you become a bonafide Python programmer in no time."
              )
    book_repo = BookRepositoryJson(id_generator=uuid_sequence_genrator()) # constrictor-based DI of id generator
    book_repo.insert(b1)
    book_repo.insert(b2)

    book_repo.save()
    book_repo.load()

    for book in book_repo.find_all():
        print(book)
