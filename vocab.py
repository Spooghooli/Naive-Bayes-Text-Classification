import os
import string

def load_dataset():
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
        lines = f.readlines()[0:12500]
        f.close()
        with open('labeledBow.feat', 'r') as f:
            lines += f.readlines()[12501:25000]
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
    k = 0
    limit = 12500
    gen = (file for file in os.listdir(os.getcwd() + r'\neg') if k < limit)
    for file in gen:
        with open(os.path.join(os.getcwd() + r'\neg', file), encoding='utf8') as f:
            lines = f.readlines()
            f.close()
            for line in lines:
                words = line.split(sep=' ')
                for w in words:
                    j += 1
        k += 1
    print(j)

    k = 0
    gen = (file for file in os.listdir(os.getcwd() + r'\pos') if k < limit)
    for file in gen:
        with open(os.path.join(os.getcwd() + r'\pos', file), encoding='utf8') as f:
            lines = f.readlines()
            f.close()
            for line in lines:
                words = line.split(sep=' ')
                for w in words:
                    i += 1
        k += 1
    print(i)

    f = open("neg_vocab.txt", "a", encoding='utf8')
    for key, value in neg_vocab.items():
        f.write(key + ':' + str(value) + '\n')
        neg_vocab[key] = value / j
    f.close()

    f = open("pos_vocab.txt", "a", encoding='utf8')
    for key, value in pos_vocab.items():
        f.write(key + ':' + str(value) + '\n')
        pos_vocab[key] = value / i
    f.close()

    f_vocab = []
    f = open("final_vocab.txt", "a", encoding='utf8')
    for w in vocabI:
        word = w
        f_vocab.append([word])
        if word in pos_vocab:
            w += '|' + str(pos_vocab[word])
            f_vocab[vocabI.index(word)].append(pos_vocab[word])
        else:
            w += '|' + str(1/(i+j))
            f_vocab[vocabI.index(word)].append(1/(i+j))
        if word in neg_vocab:
            w += '|' + str(neg_vocab[word])
            f_vocab[vocabI.index(word)].append(neg_vocab[word])
        else:
            w += '|' + str(1/(i+j))
            f_vocab[vocabI.index(word)].append(1/(i+j))
        w += '\n'
        f.write(w)


if __name__ == "__main__":
    load_dataset()

