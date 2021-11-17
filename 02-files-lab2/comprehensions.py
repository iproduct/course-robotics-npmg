

if __name__ == '__main__':
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    l = [fruit.upper() for fruit in fruits if "n" in fruit]
    print(l)
    s = {fruit.upper() for fruit in fruits if "n" in fruit}
    print(s)
    d = {fruit.upper() : len(fruit) for fruit in fruits if "n" in fruit}
    print(d)
    t = *(fruit.upper()  for fruit in fruits if "n" in fruit),
    print(t)