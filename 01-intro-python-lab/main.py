def factIter(n: int) -> int:
    acc = 1
    for i in range(1, n+1):
        acc *= i
    return acc

def factRec(n):
    if n == 1:
        return 1
    else:
        return n * factRec(n-1)

if __name__ == '__main__':
    print(factIter(500))
    print(factRec(500))


