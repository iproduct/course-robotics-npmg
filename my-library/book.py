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

if __name__ == '__main__':
    b1 = Document(1, 'Intro to Python', 'Sample presentation', 'T. Iliev', 'python, introduction')
    print(b1)