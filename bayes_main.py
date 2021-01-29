import string
import os

def get_vocabs(n, m):
    f = open('final_vocab.txt', 'r', encoding='utf8')
    lines = f.readlines()[n:m]
    f.close()

    w_pos_vocab = {}
    w_neg_vocab = {}
    pos_vocab = {}
    neg_vocab = {}
    for line in lines:
        words = line.split(sep='|')
        exclude = set('\n')
        words[2] = ''.join(ch for ch in words[2] if ch not in exclude)
        pos_vocab[words[0]] = words[1]
        neg_vocab[words[0]] = words[2]
    # print(pos_vocab)
    # print(neg_vocab)

    f = open('final_vocab.txt', 'r', encoding='utf8')
    lines = f.readlines()
    f.close()
    for line in lines:
        words = line.split(sep='|')
        exclude = set('\n')
        words[2] = ''.join(ch for ch in words[2] if ch not in exclude)
        w_pos_vocab[words[0]] = words[1]
        w_neg_vocab[words[0]] = words[2]

    return [pos_vocab, neg_vocab, w_pos_vocab, w_neg_vocab]


if __name__ == "__main__":
    vocabs = get_vocabs(300, 5000)
    cr = 0
    fr = 0
    for file in os.listdir(os.getcwd() + r'\test\pos'):
        with open(os.path.join(os.getcwd() + r'\test\pos', file), encoding='utf8') as f:
            lines = f.readlines()
            f.close()
            pos_prob = 0.5
            neg_prob = 0.5
            for line in lines:
                words = line.split(sep=' ')
                for w in words:
                    # w = w.lower()
                    # if len(w) > 1:
                    #     w = w.strip(string.punctuation)
                    if w in vocabs[0]:
                        pos_prob *= float(vocabs[0][w])
                        neg_prob *= float(vocabs[1][w])
                    elif w in vocabs[2]:
                        pos_prob *= (1-float(vocabs[2][w]))
                        neg_prob *= (1-float(vocabs[3][w]))
            if pos_prob > neg_prob:
                cr += 1
            else:
                fr += 1

    for file in os.listdir(os.getcwd() + r'\test\neg'):
        with open(os.path.join(os.getcwd() + r'\test\neg', file), encoding='utf8') as f:
            lines = f.readlines()
            f.close()
            pos_prob = 0.5
            neg_prob = 0.5
            for line in lines:
                words = line.split(sep=' ')
                for w in words:
                    # w = w.lower()
                    # if len(w) > 1:
                    #     w = w.strip(string.punctuation)
                    if w in vocabs[1]:
                        pos_prob *= float(vocabs[0][w])
                        neg_prob *= float(vocabs[1][w])
                    elif w in vocabs[3]:
                        pos_prob *= (1 - float(vocabs[2][w]))
                        neg_prob *= (1 - float(vocabs[3][w]))
            if neg_prob > pos_prob:
                cr += 1
            else:
                fr += 1

    print(str(cr/100)+'%')
    print(cr, fr)