import string

def load_dataset(filename, vocab):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    with open(vocab, encoding='utf8') as f:
        stoplines = f.readlines()[0:50]
    f.close()
    stopwords = {}
    for s in stoplines:
        exclude = set('\n')
        s = ''.join(ch for ch in s if ch not in exclude)
        stopwords[s] = None

    dataset = []
    for line in lines:
        attributes = line.split(sep=' ')
        data = []
        for a in attributes:
            exclude = set(string.punctuation)
            a = ''.join(ch for ch in a if ch not in exclude)
            a = a.lower()
            if a in stopwords:
                data.append(1)
            else:
                data.append(0)
        dataset.append(data)
    return dataset


if __name__ == "__main__":
    data = []
    data.append(load_dataset('0_9.txt', 'imdb.vocab'))
    data.append(load_dataset('1_7.txt', 'imdb.vocab'))
    print(data)

