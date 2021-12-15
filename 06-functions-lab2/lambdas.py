
if __name__ == "__main__":
    def myfunc(n):  # factory, closure = enclosing scope
        return lambda a: a * n


    mydoubler = myfunc(2)
    mytripler = myfunc(3)
    print(mydoubler)
    print(mytripler)
    print(mydoubler(11))
    print(mytripler(12))