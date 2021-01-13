import re

def myFunc(item):
    return item[1]

if __name__ == "__main__":
    file = open("wikipedia.txt", "rt", encoding="utf-8")

    counts = dict()

    for line in file:
        words = set(re.split("[\s\.,?!\[\]\(\)\'\"=:;]+", line))
        # print(words)
        for w in words:
            if(len(w) <= 3):
                continue
            if(w in counts):
                counts[w] = counts[w] + 1
            else:
                counts[w] = 1

    wlist = list(counts.items())
    wlist.sort(reverse=True, key=myFunc)
    print(wlist[:10])