
if __name__ == '__main__':
    print(ord('ю'))
    print(chr(1102))
    s = 'abcdю'
    e = enumerate(s)
    for i, c in e:
        print(f'{i} -> {c}')
    b = s.encode('utf8')
    print(b)