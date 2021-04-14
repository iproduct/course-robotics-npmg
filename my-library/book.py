class Document:
    def __init__(self, id, title, subtitle, authors, tags, language='EN'):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.tags = tags
        self.language = language

    def __str__(self):
        return f'ID: {self.id}, Title: {self.title}, Subtitle: {self.subtitle}, Authors: {self.authors}, ' \
               f'Tags: {self.tags}, Language: {self.language}'

class Book(Document):
    def __init__(self, id, title, subtitle, authors, tags, year, language='EN'):
        Document.__init__(self, id, title, subtitle, authors, tags, language) # call constructor of the base class
        self.year = year
    def __str__(self):
        return f'Book({Document.__str__(self)}, Year: {self.year})'

if __name__ == '__main__':
    d1 = Document(1, 'Intro to Python', 'Sample presentation', 'T. Iliev', 'python, introduction')
    print(d1)
    b2 = Book(2, 'Learning Python', 'Powerfull Object-Oriented Programming', 'David Ascher, Mark Lutz', 'python, learning, OOP', 1999)
    print(b2)