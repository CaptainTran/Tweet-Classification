from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.model_selection import KFold
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import numpy as np


def report_results(accuracy, precision, recall, fscore, candidate_name):
    strings = ['negative', 'neutral', 'positive']
    print(candidate_name, "accuracy", accuracy)
    for idx, i in enumerate(strings):
        if idx != 1:
            print(candidate_name, i, "precision:", precision[idx])
            print(candidate_name, i, "recall:", recall[idx])
            print(candidate_name, i, "fscore:", fscore[idx])


def get_unique(labels):
    output = set()
    for x in labels:
        output.add(x)
    labels = list(output)
    labels.sort()
    return labels


class NBClassifier:

    nbclassifier = None
    candidate_name = None
    predicted = None

    def __init__(self, candidate_name):
        self.candidate_name = candidate_name

    def train(self, train_data, train_labels):
        self.nbclassifier = MultinomialNB().fit(train_data, train_labels)

    def test(self, test_data, test_labels):
        # true = []
        pred = []
        for idx, i in enumerate(test_labels):
            # true.append(i)
            pred.append(self.nbclassifier.predict(test_data[idx]))
        # accuracy = accuracy_score(true, pred)
        # precision = precision_score(true, pred, average=None)
        # recall = recall_score(true, pred, average=None)
        # fscore = f1_score(true, pred, average=None)
        # report_results(accuracy, precision, recall, fscore)
        self.predicted = pred

    def cross_validation(self, train_data, train_labels):

        predictor = MultinomialNB()

        num_labels = len(get_unique(train_labels))
        accuracy = 0
        precision = np.zeros(num_labels)
        recall = np.zeros(num_labels)
        fscore = np.zeros(num_labels)
        num_folds = 10
        k_fold = KFold(n_splits=num_folds)
        for train_indices, test_indices in k_fold.split(train_data):
            x_train = train_data[train_indices]
            y_train = [train_labels[i] for i in train_indices]

            x_test = train_data[test_indices]
            y_test = [train_labels[i] for i in test_indices]

            predictor.fit(x_train, y_train)
            y_pred = predictor.predict(x_test)

            accuracy += accuracy_score(y_test, y_pred)
            precision += precision_score(y_test, y_pred, average=None)
            recall += recall_score(y_test, y_pred, average=None)
            fscore += f1_score(y_test, y_pred, average=None)

        accuracy /= num_folds
        precision /= num_folds
        recall /= num_folds
        fscore /= num_folds
        report_results(accuracy, precision, recall, fscore, self.candidate_name)


class SVMClassifier:

    svmclassifier = None
    candidate_name = None
    predicted = None

    def __init__(self, candidate_name):
        self.candidate_name = candidate_name

    def train(self, train_data, train_labels):
        self.svmclassifier = LinearSVC().fit(train_data, train_labels)

    def test(self, test_data, test_labels):
        # true = []
        pred = []
        for idx, i in enumerate(test_labels):
            # true.append(i)
            pred.append(self.nbclassifier.predict(test_data[idx]))
        # accuracy = accuracy_score(true, pred)
        # precision = precision_score(true, pred, average=None)
        # recall = recall_score(true, pred, average=None)
        # fscore = f1_score(true, pred, average=None)
        # report_results(accuracy, precision, recall, fscore)
        self.predicted = pred

    def cross_validation(self, train_data, train_labels):

        predictor = LinearSVC()

        num_labels = len(get_unique(train_labels))
        accuracy = 0
        precision = np.zeros(num_labels)
        recall = np.zeros(num_labels)
        fscore = np.zeros(num_labels)
        num_folds = 10
        k_fold = KFold(n_splits=num_folds)
        for train_indices, test_indices in k_fold.split(train_data):
            x_train = train_data[train_indices]
            y_train = [train_labels[i] for i in train_indices]

            x_test = train_data[test_indices]
            y_test = [train_labels[i] for i in test_indices]

            predictor.fit(x_train, y_train)
            y_pred = predictor.predict(x_test)

            accuracy += accuracy_score(y_test, y_pred)
            precision += precision_score(y_test, y_pred, average=None)
            recall += recall_score(y_test, y_pred, average=None)
            fscore += f1_score(y_test, y_pred, average=None)

        accuracy /= num_folds
        precision /= num_folds
        recall /= num_folds
        fscore /= num_folds
        report_results(accuracy, precision, recall, fscore, self.candidate_name)