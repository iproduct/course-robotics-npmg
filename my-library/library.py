import re
from book import Book

LANGUAGES = ['English', 'Bulgarian', 'German', 'Russian']

def input_book():
    #input title
    while True:
        title = input('Input title:')
        if len(title) >= 3:
            break
        print('Error: title should be atleast 3 characters long.')

    #input subtitle
    subtitle = input('Input Subtitle:')

    # input authors
    while True:
        answer = input('Input authors (comma separated):')
        if len(answer) >= 5:
            authors = answer.split(',')
            i = 0
            while i < len(authors):
                authors[i] = authors[i].strip()
                if authors[i] == '':
                    authors.pop(i)
                    continue
                if len(authors[i]) < 5:
                    break
                else:
                    i += 1
            if i == len(authors):
                break
        print('Error: each author name should be at least 5 characters long.')

    # input tags
    while True:
        answer = input('Input tags (comma separated):')
        if len(answer) >= 2:
            tags = answer.split(',')
            i = 0
            while i < len(tags):
                tags[i] = tags[i].strip()
                if tags[i] == '':
                    tags.pop(i)
                    continue
                if len(tags[i]) < 2:
                    break
                else:
                    i += 1
            if i == len(tags):
                break
        print('Error: each tag should be at least 2 characters long.')

    # input year
    while True:
        year = input('Input publishing year:')
        if re.match(r'[12][0-9]{3}', year):
            break
        print('Error: invalid year - try again.')

    # input language
    while True:
        langIndex = input('Input language 1) English, 2) Bulgarian, 3) German, 4) Russian:')
        if re.match(r'[1-4]', langIndex):
            language = LANGUAGES[int(langIndex) - 1]
            break
        print('Error: invalid language choice - try again.')

    return Book(None, title, subtitle, authors, tags, year, language)

def print_books(books):
    print('-' * 170)
    print(f'| {"ID":4} | {"Title":35} | {"Subtitle":35.35} | {"Authors":30} | {"Tags":30} | {"Year":6} | {"Language":8} |')
    print('-' * 170)
    for b in books:
        print(
            f'| {b.id:4} | {b.title:35.35} | {b.subtitle:35.35} | {b.authors:30.30} | {", ".join(b.tags):30.30} | {b.year:6} | {b.language:8.8} |')
    print('-' * 170)


if __name__ == '__main__':
    # b1 = input_book()
    tags = 'python, learning, OOP'.split(", ")
    for i in range(len(tags)):
        tags[i] = tags[i].strip()

    b2 = Book(2, 'Learning Python', 'Powerfull Object-Oriented Programming', 'David Ascher, Mark Lutz',
              tags, 1999)
    b3 = Book(3, 'Python for Everybody', 'Powerfull Object-Oriented Programming', 'David Ascher, Mark Lutz',
              tags, 2020)
    b4 = Book(4, 'Python by Example', 'Powerfull Object-Oriented Programming', 'Hristo Petrov',
              tags, 2019, "BG")
    print_books([b2, b3, b4])




