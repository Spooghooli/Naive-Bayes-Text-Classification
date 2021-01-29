import string
import os

def load_dataset(filename, vocab):
    w_pos_vocab = {}
    w_neg_vocab = {}
    f = open('final_vocab.txt', 'r', encoding='utf8')
    line = f.readline()
    while(line != ''):
        words = line.split(sep='|')
        exclude = set('\n')
        words[2] = ''.join(ch for ch in words[2] if ch not in exclude)
        w_pos_vocab[words[0]] = words[1]
        w_neg_vocab[words[0]] = words[2]
        line = f.readline()
    f.close()

    # for line in lines:
    #     words = line.split(sep=':')
    #     exclude = set('\n')
    #     words[2] = ''.join(ch for ch in words[2] if ch not in exclude)
    #     w_pos_vocab[words[0]] = words[1]
    #     w_neg_vocab[words[0]] = words[2]
    # w_pos_vocab['do'] = str(0.00131341645103113)
    for file in os.listdir(os.getcwd() + r'\test\pos'):
        with open(os.path.join(os.getcwd() + r'\test\pos', file), encoding='utf8') as f:
            lines = f.readlines()
            f.close()
            pos_prob = 0.5
            neg_prob = 0.5
            for line in lines:
                words = line.split(sep=' ')
                for w in words:
                    if w in w_pos_vocab:
                        print(w)
                        print(w_pos_vocab[w]+'!')
                        print(w_neg_vocab[w]+'!')
                        pos_prob *= (1-float(w_pos_vocab[w]))
                        neg_prob *= (1-float(w_neg_vocab[w]))
            # if pos_prob > neg_prob:
            #     cr += 1
            # else:
            #     fr += 1

if __name__ == "__main__":
    data = []
    data.append(load_dataset('0_9.txt', 'imdb.vocab'))
    data.append(load_dataset('1_7.txt', 'imdb.vocab'))
    print(data)

