def fib():
    # Връща при поредно извикване поредното число на # Фибоначи
    a, b, index = 0, 1, 0
    while index < 5:
        yield (a)
        a, b, index = b, a + b, index + 1


if __name__ == "__main__":
    # Всяка нова стойност се инициира с обръщението
    # next()
    f = fib()
    for i in range(10):
        try:
            print(next(f))
        except StopIteration:
            print("finished.")
            break

