from sklearn import svm
from sklearn import datasets
from joblib import dump


X, y = datasets.load_iris(return_X_y=True)
clf = svm.SVC()
clf.fit(X, y)
dump(clf, 'clf.joblib')
for i in range(1, 100):
    print(list(X[i]))
    print(i, y[i])
