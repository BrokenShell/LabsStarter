from sklearn import svm, datasets
from joblib import dump


X, y = datasets.load_iris(return_X_y=True)
model = svm.SVC(probability=True)
model.fit(X, y)
dump(model, '../project/app/api/model.joblib')
