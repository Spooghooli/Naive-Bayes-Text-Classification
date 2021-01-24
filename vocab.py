import os
import string
from difflib import SequenceMatcher

def load_dataset(filename, vocab):
    neg_vocab = {}
    pos_vocab = {}
    i = 0
    j = 0
    for file in os.listdir(os.getcwd() + r'\pos'):
        with open(os.path.join(os.getcwd() + r'\pos', file), encoding='utf8') as f:
            lines = f.readlines()
            f.close()
            for line in lines:
                words = line.split(sep=' ')
                for w in words:
                    # w = w.strip('<br')
                    # w = w.strip(')')
                    # w = w.strip('(')
                    # w = w.strip('.')
                    # w = w.strip(string.punctuation)
                    exclude = set(string.punctuation)
                    w = ''.join(ch for ch in w if ch not in exclude)
                    w = w.lower()
                    i += 1
                    if w in neg_vocab:
                        neg_vocab[w] += 1
                    else:
                        neg_vocab[w] = 1
    print(neg_vocab)
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


if __name__ == "__main__":
    load_dataset('0_9.txt', 'imdb.vocab')

