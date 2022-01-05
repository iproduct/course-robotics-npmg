class Book(object):
    """Book model class"""

    def __init__(self, id=None, title=None, subtitle=None, authors=[], isbn=None,
                 publisher=None, year=None, price=None, genre="programming", tags=[], description=None):
       self.id = id
       self.title = title
       self.subtitle = subtitle
       self.authors = authors
       self.isbn = isbn
       self.publisher = publisher
       self.year = year
       self.price = price
       self.genre = genre
       self.tags = tags
       self.description = description

    def __str__(self):
        return f"| {self.id:^3.3s} | {self.title:<22.22s} | {self.subtitle:<22.22s} | " \
               f"{','.join(self.authors):^25.25s} | {self.isbn:^10.10s} | {self.publisher:^10.10s} | " \
               f"{self.year:<4d} | {self.price:<6.2f} | {self.genre:<15.15s} | " \
               f"{','.join(self.tags):^25.25s} |"

