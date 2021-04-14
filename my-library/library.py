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

if __name__ == '__main__':
    b1 = input_book()
    print(b1)




