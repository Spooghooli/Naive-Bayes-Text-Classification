import math
from dataLoader import *
from bayes import *


def training_results():
    # witch percentage of data will take each set of data used for training, validation and testing of the algorithm
    train = 0.6
    test = 0.4

    nb = NaiveBayes()

    data_file = 'dermatology.csv'
    dataset = load_dataset(filename=data_file)

    # splitting the data
    training_data = dataset[:math.floor(train * len(dataset))]
    test_data = dataset[math.floor(test * len(dataset)):]

    categories = [1, 0]
    feature_values = nb.extract_feature_values(dataset)
    nb.train(training_data, categories, feature_values)

    # creating the array of test_data responses
    y = []
    for d in test_data:
        y.append(d[-1])

    # creating the array of training_data responses
    x = []
    for d in training_data:
        x.append(d[-1])

    # computing the measures both on training data end on test data
    measures_for_train = get_metrics(get_results(nb.response_all(training_data), x))
    measures_for_test = get_metrics(get_results(nb.response_all(test_data), y))

    print("*******Training data*******\n" + str_metrics(measures_for_train))
    print("*******Test data*******\n" + str_metrics(measures_for_test))


'''
return an array of the form
+---------+
| tp | fp |
+----+----+
| tn | fn |
+---------+
cr ----> correct response
r  ----> response
'''


def get_results(cr, r):
    tp = 0
    fp = 0
    tn = 0
    fn = 0

    for i in range(len(cr)):
        if cr[i] == 1:
            if r[i] == 1:
                tp += 1
            else:
                fn += 1
        else:
            if r[i] == 0:
                tn += 1
            else:
                fp += 1

    return [[tp, fp], [tn, fn]]


'''
returns a list of the form [accuracy, precision, recall, f-measure]
'''


def get_metrics(results):
    tp = results[0][0]
    tn = results[1][0]
    fp = results[0][1]
    fn = results[1][1]

    metrics = [0,0,0,0]
    # accuracy
    metrics[0] = (tp + tn) / (tp + tn + fp + fn)
    # precision
    try:
        metrics[1] = tp / (tp + fp)
    except ZeroDivisionError as z:
        metrics[1] = 'inf'
    # recall
    try:
        metrics[2] = tp / (tp + fn)
    except ZeroDivisionError as z:
        metrics[2] = 'inf'
    # f-measure
    try:
        if metrics[1] == 'inf' or metrics[2] == 'inf':
            metrics[3] = 'NA'
        else:
            metrics[3] = (2 * metrics[1] * metrics[2]) / (metrics[1] + metrics[2])
    except ZeroDivisionError as z:
        metrics = 'inf'

    return metrics


def str_metrics(metrics):
    return 'accuracy: ' + str(metrics[0]) + '\nprecision: ' + str(metrics[1]) + '\nrecall: ' + str(metrics[2]) + '\nf-measure: ' + \
           str(metrics[3])


if __name__ == "__main__":
    training_results()
