import pickle
import spacy


def predict(txt):
    nlp = spacy.load('en_core_web_md')
    file = open('final_model.sav', 'rb')
    clf2 = pickle.load(file)
    doc = nlp(txt)
    X = []
    for t in txt:
        doc = nlp(t)
        X.append(doc.vector)
    return clf2.predict(X)

