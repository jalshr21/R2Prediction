import spacy
from R2Prediction.src.data import reading
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import f1_score
import pickle

def fit():
    nlp = spacy.load('en_core_web_md')
    data = reading.readSqliteData('db.sqlite')
    X = []
    y = []
    for index, row in data.iterrows():
        doc = nlp(row['text'])
        label = row['class_label']
        X.append(doc.vector)
        y.append(label)
    X = np.array(X)
    X_train = X[:9000]
    y_train = y[:9000]
    X_test = X[9000:]
    y_test = y[9000:]
    clf = SVC(gamma='auto', class_weight="balanced")
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(f1_score(y_pred, y_test, average='weighted'))

    #Save model
    filename = 'final_model.sav'
    pickle.dump(clf, open(filename, 'wb'))


if __name__ == '__main__':
    fit()