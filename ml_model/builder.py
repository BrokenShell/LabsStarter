from sklearn import svm, datasets
from joblib import dump


X, y = datasets.load_iris(return_X_y=True)
clf = svm.SVC(probability=True)
clf.fit(X, y)
dump(clf, '../project/app/api/clf.joblib')
