
def my_index(list, elem, index):
    try:
        result = list.index(elem, index)
    except:
        return -1
    return result

if __name__ == '__main__':
    l = list(range(1,10))
    l.insert(5, 2)
    l.insert(7, 2)
    print(l)
    # print(l.count(2))

    found = 0
    while found >= 0:
        found = my_index(l, 2, found)
        if found >= 0:
            print(found)
            found = found + 1

    for i in range(0,len(l)):
        if l[i] == 2:
            print(i)

    for i, v in enumerate(l):
        if v == 2:
            print(i)