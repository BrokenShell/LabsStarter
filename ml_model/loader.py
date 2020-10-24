from joblib import load
from sklearn import datasets


model = load('../project/app/api/clf.joblib')


if __name__ == '__main__':
    X, y = datasets.load_iris(return_X_y=True)
    for i in range(len(X)):
        data = list(X[i])
        pred = model.predict([X[i]])[0]
        y_true = y[i]
        proba = max(model.predict_proba([X[i]])[0])
        print(f'#{i} {data}: {pred}/{y_true} @ {100 * proba:.0f}%')
