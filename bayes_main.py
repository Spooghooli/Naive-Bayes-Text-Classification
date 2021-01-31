import string
import os
from math import floor


def get_vocabs(n, m):
    choice = input("How much of the training data do you wish to use? \nAnswer 1 for 5%, 2 for 25%, 3 for 50%, 4 for 75%, 5 for 100%: ")
    d = os.getcwd()
    choice = int(choice)
    if choice == 1:
        d += r"\vocabs\5%"
    if choice == 2:
        d += r"\vocabs\25%"
    if choice == 3:
        d += r"\vocabs\50%"
    if choice == 4:
        d += r"\vocabs\75%"
    if choice == 5:
        d += r"\vocabs\100%"
    d += r"\final_vocab.txt"

    f = open('%s' % d, 'r', encoding='utf8')
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

    f = open('%s' % d, 'r', encoding='utf8')
    lines = f.readlines()
    f.close()
    for line in lines:
        words = line.split(sep='|')
        exclude = set('\n')
        words[2] = ''.join(ch for ch in words[2] if ch not in exclude)
        w_pos_vocab[words[0]] = words[1]
        w_neg_vocab[words[0]] = words[2]

    return [pos_vocab, neg_vocab, w_pos_vocab, w_neg_vocab]

def bayes(path):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    i = 0
    limit = int(input("Set testing data limit (review number): "))
    n = int(input("Set n: "))
    m = int(input("Set m: "))
    vocabs = get_vocabs(n, m)  # 300 5000
    gen = (file for file in os.listdir(path + r'\pos') if i < limit)
    for file in gen:
        with open(os.path.join(path + r'\pos', file), encoding='utf8') as f:
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
                        pos_prob *= (1 - float(vocabs[2][w]))
                        neg_prob *= (1 - float(vocabs[3][w]))
            if pos_prob > neg_prob:
                tp += 1
            else:
                fp += 1
        i += 1

    i = 0
    gen = (file for file in os.listdir(path + r'\neg') if i < limit)
    for file in gen:
        with open(os.path.join(path + r'\neg', file), encoding='utf8') as f:
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
                tn += 1
            else:
                fn += 1
        i += 1

    accuracy = (tp + tn) / (tp + tn + fp + fn)
    precision = (tp / (tp + fp))
    recall = (tp / (tp + fn))
    f1 = (2 * precision * recall) / (precision + recall)
    print("Accuracy: " + str(floor(accuracy * 100)) + '%')
    print("Precision: " + str(precision))
    print("Recall: " + str(recall))
    print("F1: " + str(f1))
    print(tp, tn, fp, fn)

if __name__ == "__main__":
    print("----- Test Data -----")
    bayes(os.getcwd() + r"\test")
    print("----- Training Data -----")
    bayes(os.getcwd())
