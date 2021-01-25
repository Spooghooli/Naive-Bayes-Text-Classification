import os
import string
from difflib import SequenceMatcher

def load_dataset(filename, vocab):
    neg_vocab = {}
    pos_vocab = {}
    vocabI = []
    i = 0
    j = 0
    f = open('imdb.vocab', encoding='utf8')
    l = f.readlines()
    f.close()

    for v in l:
        exclude = set('\n')
        v = ''.join(ch for ch in v if ch not in exclude)
        neg_vocab[v] = 1
        pos_vocab[v] = 1
        vocabI.append(v)
    print(vocabI)

    with open('labeledBow.feat', 'r') as f:
        lines = f.readlines()
        f.close()
        for line in lines:
            words = line.split(sep=' ')
            if int(words[0]) > 5:
                words.pop(0)
                for w in words:
                    w = w.split(sep=':')
                    pos_vocab[vocabI[int(w[0])]] += int(w[1])
            else:
                words.pop(0)
                for w in words:
                    w = w.split(sep=':')
                    neg_vocab[vocabI[int(w[0])]] += int(w[1])
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

    dictionary_items = neg_vocab.items()
    sorted_items = sorted(dictionary_items)
    print(sorted_items)
    f = open("demofile3.txt", encoding='utf8' "a")
    for key, value in neg_vocab.items():
        f.write('('+key+','+str(value)+')')
    f.close()

    for file in os.listdir(os.getcwd() + r'\neg'):
        with open(os.path.join(os.getcwd() + r'\neg', file), encoding='utf8') as f:
            lines = f.readlines()
            f.close()
            for line in lines:
                words = line.split(sep=' ')
                data = []
                for w in words:
                    j += 1
    print(j)

    for file in os.listdir(os.getcwd() + r'\pos'):
        with open(os.path.join(os.getcwd() + r'\pos', file), encoding='utf8') as f:
            lines = f.readlines()
            f.close()
            for line in lines:
                words = line.split(sep=' ')
                data = []
                for w in words:
                    i += 1
    print(i)


if __name__ == "__main__":
    load_dataset('0_9.txt', 'imdb.vocab')

