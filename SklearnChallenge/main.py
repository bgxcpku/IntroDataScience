import csv
import numpy as np
from sklearn import svm
from sklearn import decomposition
from sklearn import cross_validation as cv
from sklearn import grid_search as gs
from sklearn import metrics
import datetime as dt


def data_read():
    '''Reading the data'''
    na_train_data = np.zeros((1000, 40))
    reader = csv.reader(open('train.csv', 'rU'), delimiter=',')
    for i, row in enumerate(reader):
        na_train_data[i] = [float(x) for x in row]

    na_train_label = np.zeros(1000)
    reader = csv.reader(open('trainLabels.csv', 'rU'), delimiter=',')
    for i, row in enumerate(reader):
        na_train_label[i] = float(row[0])
        
    na_test_data = np.zeros((9000, 40))
    reader = csv.reader(open('test.csv', 'rU'), delimiter=',')
    for i, row in enumerate(reader):
        na_test_data[i] = [float(x) for x in row]

    return na_train_data, na_train_label, na_test_data


def decomposition_pca(na_train_data, na_test_data):
    """ Linear dimensionality reduction """
    pca = decomposition.PCA(n_components=12, whiten=True)
    na_train_pca = pca.fit_transform(na_train_data)
    na_test_pca = pca.transform(na_test_data)
    return na_train_pca, na_test_pca


def validation(clf, X_validation, Y_validation):
    '''Score the validation set'''
    Y_pred_val = clf.predict(X_validation)
    print metrics.classification_report(Y_validation.astype(np.int), Y_pred_val)


def learning(na_train_data, na_train_label):
    '''Learning the model'''
    X_train, X_validation, Y_train, Y_validation = cv.train_test_split(
                na_train_data, na_train_label, test_size=0.1, random_state=0)
    clf = svm.SVC()
    clf.fit(X_train, Y_train)
    return clf, X_validation, Y_validation


def query(clf, na_test_data):
    '''Querying the test data'''
    na_test_label = clf.predict(na_test_data)
    writer = csv.writer(open('testLabels.csv', 'wb'), delimiter=',')
    for val in na_test_label:
        writer.writerow([int(val)])
    return


def main():
    '''Main Function'''

    dt_orig = dt.datetime.now()
    
    # print "Reading the data"
    # dt_start = dt.datetime.now()
    na_train_data, na_train_label, na_test_data = data_read()
    # print "Reading in : ", (dt.datetime.now() - dt_start).total_seconds()

    # print "Reduction of data"
    # dt_start = dt.datetime.now()
    na_train_data, na_test_data = decomposition_pca(na_train_data, na_test_data)
    # print "Reduction in : ", (dt.datetime.now() - dt_start).total_seconds()

    # print "Learning the model"
    # dt_start = dt.datetime.now()
    clf, X_validation, Y_validation = learning(na_train_data, na_train_label)
    # print "Learning in : ", (dt.datetime.now() - dt_start).total_seconds()

    # print "Validation the model"
    # dt_start = dt.datetime.now()
    validation(clf, X_validation, Y_validation)
    # print "Validation in : ", (dt.datetime.now() - dt_start).total_seconds()

    # print "Querying the test set"
    # dt_start = dt.datetime.now()
    query(clf, na_test_data)
    # print "Querying in : ", (dt.datetime.now() - dt_start).total_seconds()

    print "Done in : ", (dt.datetime.now() - dt_orig).total_seconds()


if __name__ == '__main__':
    print "Kaggle Sklearn Challenge"
    main()
