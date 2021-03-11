if __name__ == '__main__':
    f = open('files.py', 'rt')
    lines = f.readlines()
    # print(lines)
    i = 1
    for line in lines:
        print(f'{i}: {line}')
        i += 1