import string

class Bayes:

    def __init__(self):
        self.c_counter = None
        self.feature_values = None
        self.num_in_each_category = None

    def load_dataset(filename, vocab):
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        with open(vocab, encoding='utf8') as f:
            stoplines = f.readlines()
        f.close()
        stopwords = {}
        for s in stoplines:
            exclude = set('\n')
            s = ''.join(ch for ch in s if ch not in exclude)
            stopwords[s] = None

        # for w in words:
        #     exclude = set(string.punctuation)
        #     w = ''.join(ch for ch in w if ch not in exclude)
        #     w = w.lower()
        #     i += 1
        #     if w in vocabI and w not in neg_vocab:
        #         neg_vocab[w] = 1
        #     elif w in vocabI and w in neg_vocab:
        #         neg_vocab[w] += 1
        #     else:
        #         for v in vocabI:
        #             if SequenceMatcher(None, w, v).ratio() > 0.7:
        #                 if v in neg_vocab:
        #                     neg_vocab[v] += 1
        #                     print(v)
        #                     break
        #                 else:
        #                     neg_vocab[v] = 1
        #                     print(v)
        #                     break

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

    # def transpose(data):
    #     dataT = [[]] * len(data[0])
    #     for d in data:
    #         for i in range(len(d)):
    #             if d[i] not in dataT[i]:
    #                 dataT[i].append(d[i])
    #     return dataT

    # gia ka8e feature kai gia ka8e pi8ani timi tou feature a8roizei posa paradeigmata einai se ka8e katigoria
    # def get_values_counts(data, feature_values, categories):
    #     # categories -> a list of the possible categories
    #     counter = []
    #     for feature in feature_values:
    #         counter.append(dict.fromkeys(feature, dict.fromkeys(categories, 0)))
    #     for d in data:
    #         for i in range(len(d) - 1):  # to d[-1] einai i apokrisi
    #             counter[i].get(d[i])[d[-1]] += 1
    #     return counter

    if __name__ == "__main__":
       load_dataset('0_9.txt', 'imdb.vocab')
