from functools import reduce

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    # myreducer = reduce(lambda acc, elem: acc + elem, numbers, 0)
    # myreducer = reduce(lambda acc, elem: acc * elem, numbers, 1)
    myreducer = reduce(lambda acc, elem: str(acc) + str(elem), numbers, "")
    print("reducer = ", myreducer)
