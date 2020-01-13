import pickle
import en_core_web_sm

def predict(txt):
    nlp = en_core_web_sm.load()
    file = open('/Users/shrutijalan/CICD-Flask/R2Prediction/src/scripts/final_model.sav', 'rb')
    clf2 = pickle.load(file)
    X = []
    for t in txt:
        doc = nlp(t)
        X.append(doc.vector)
    return clf2.predict(X)

