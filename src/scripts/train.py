import spacy
from R2Prediction.src.data import reading
import numpy as np
from sklearn.svm import SVC

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
    clf = SVC(gamma='auto')
    clf.fit(X_train, y_train)
