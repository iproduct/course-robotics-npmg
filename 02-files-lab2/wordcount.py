import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stops = set(stopwords.words('english'))
# print(stops)
# print()

def get_count(wordcount_tupple):
    return wordcount_tupple[1]

if __name__ == '__main__':
    # file = open("wikipedia.txt", "rt")
    with open("wikipedia.txt", "rt") as file:
        wordcounts = dict()
        for line in file:
            line  = line.strip()
            if len(line) == 0: # if line is emepty
                continue
            for word in line.split():
                if len(word) < 2 or word in stops:
                    continue
                wordcounts[word] = wordcounts.get(word, 0) + 1

    wc_list = [(word, wordcounts[word]) for word in wordcounts]
    wc_list.sort(key = get_count, reverse=True)
    for wc in wc_list[:10]:
        print(wc[0], "->", wc[1])