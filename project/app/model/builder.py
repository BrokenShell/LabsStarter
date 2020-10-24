from sklearn import svm
from sklearn import datasets
from joblib import dump


X, y = datasets.load_iris(return_X_y=True)
clf = svm.SVC()
clf.probability = True
clf.fit(X, y)
dump(clf, 'clf.joblib')

print(clf.predict([X[0]])[0])
print(max(clf.predict_proba([X[0]])[0]))

# for i in range(1, 100):
#     print(list(X[i]))
#     print(i, y[i])
