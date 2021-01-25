import os
import string

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

    print(neg_vocab)
    f = open("neg_vocab.txt", "a", encoding='utf8')
    for key, value in neg_vocab.items():
        f.write(key+':'+str(value)+'\n')
    f.close()

    print(pos_vocab)
    f = open("pos_vocab.txt", "a", encoding='utf8')
    for key, value in pos_vocab.items():
        f.write(key+':'+str(value)+'\n')
    f.close()

    for file in os.listdir(os.getcwd() + r'\neg'):
        with open(os.path.join(os.getcwd() + r'\neg', file), encoding='utf8') as f:
            lines = f.readlines()
            f.close()
            for line in lines:
                words = line.split(sep=' ')
                for w in words:
                    j += 1
    print(j)

    for file in os.listdir(os.getcwd() + r'\pos'):
        with open(os.path.join(os.getcwd() + r'\pos', file), encoding='utf8') as f:
            lines = f.readlines()
            f.close()
            for line in lines:
                words = line.split(sep=' ')
                for w in words:
                    i += 1
    print(i)


if __name__ == "__main__":
    load_dataset('0_9.txt', 'imdb.vocab')

