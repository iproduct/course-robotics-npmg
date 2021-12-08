if __name__ == "__main__":
    with open("readlines.py", "rt") as f:
        text = f.read()
        print(text)

    # f = open("readlines.py", "rt")
    # print(f.readline())
    # f.close()

    with open("readlines.py", "rt") as f:
        line = f.readline()
        while len(line) > 0:
            print(line.strip(), end="\n")
            line = f.readline()

    with open("readlines.py", "rt") as f:
        for line in f:
            print(line, end="")

    with open("readlines.py", "rt") as f:
        for index, line in enumerate(f):
            print(index + 1, ":", line, end="")
