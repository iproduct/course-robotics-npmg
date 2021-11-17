
if __name__ == '__main__':
    # file = open("wikipedia.txt", "rt")
    with open("wikipedia.txt", "rt") as file:
        lines = [line for line in file if len(line.strip()) > 0]
        words = dict()
        for line in lines:
            words.update({word for word in line.split()})

        n = 0
        for word in words:
            n += 1
            print(n, ":", word, end="\n")
    # file.close()