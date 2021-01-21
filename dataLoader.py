import string

def load_dataset(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    with open('imdb.vocab', encoding='utf8') as f:
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


# def transpose(data):
#     dataT = [[]] * len(data[0])
#     for d in data:
#         for i in range(len(d)):
#             if d[i] not in dataT[i]:
#                 dataT[i].append(d[i])
#     return dataT



# gia ka8e feature kai gia ka8e pi8ani timi tou feature a8roizei posa paradeigmata einai se ka8e katigoria
def get_values_counts(data, feature_values, categories):
    # categories -> a list of the possible categories
    counter = []
    for feature in feature_values:
        counter.append(dict.fromkeys(feature, dict.fromkeys(categories, 0)))
    for d in data:
        for i in range(len(d) - 1):  # to d[-1] einai i apokrisi
            counter[i].get(d[i])[d[-1]] += 1
    return counter


if __name__ == "__main__":
    data = []
    data.append(load_dataset('0_9.txt'))
    data.append(load_dataset('1_7.txt'))
    print(data)

