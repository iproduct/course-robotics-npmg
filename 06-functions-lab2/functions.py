from functools import reduce

books = [
    {"id": 1, "title": "Learning Python", "subtitle": "", "authors": ["Марк Лътз", "Дейвид Асър"],
     "publisher": "O'Reily", "year": 1999, "price": 22.7},
    {"id": 2, "title": "Think Python", "subtitle": "An Introduction to Software Design", "authors": ["Алън Б. Дауни"],
     "publisher": "O'Reily", "year": 2002, "price": 9.4},
    {"id": 3, "title": "Python Cookbook", "subtitle": "Recipes for Mastering Python 3",
     "authors": ["Браян К. Джоунс", "Дейвид М. Баазли"], "publisher": "O'Reily", "year": 2011, "price": 135.9}
]

if __name__ == "__main__":
    for b in books:
        print(
            f"| {b['id']:^3d} | {b['title']:<20.20s} | {b['subtitle']:<20.20s} | {', '.join(b['authors']):<25.25s} |"
            f" {b['publisher']:^10.10s} | {b['year']:<4d} | {b['price']:>7.2f} |")

    # print list of all book titles
    titles = []
    for book in books:
        titles.append(book['title'])

    print(titles)

    # using higer order function - map
    titles = map(lambda book: book['title'], books)

    print(titles)
    # for title in titles:
    #     print(title)

    print(list(titles))
    titles = map(lambda book: book['title'], books)
    print(tuple(titles))
    titles = map(lambda book: book['title'], books)
    print(set(titles))
    titles = map(lambda book: book['title'], books)
    print(dict.fromkeys(titles, 0))

    # using comprehensions
    titles = [book['title'] for book in books]
    print("Using list comprehension:", titles)
    titles_set = {book['title'] for book in books}
    print("Using set comprehension:", titles_set)
    titles_price_dict = { book['title'] : book['price'] for book in books}
    print("Using dict comprehension:", titles_price_dict)

    # calculate all books price
    total = reduce(lambda acc, price: acc + price, map(lambda book: book['price'], books), 0)
    print("All books total:", total)

    titles = list(map(lambda b: b['title'], books))
    subtitles = list(map(lambda b: b['subtitle'], books))
    prices = list(map(lambda b: b['price'], books))

    print(titles)
    print(subtitles)
    print(prices)

    book_tuples = list(zip(titles, subtitles, prices))
    print(book_tuples)
    book_tuples.sort(key = lambda btup: btup[2], reverse=True)
    print(book_tuples)
    print( sorted(book_tuples, key = lambda btup: btup[2]))