from joblib import load
from sklearn import datasets


model = load('clf.joblib')


if __name__ == '__main__':
    X, y = datasets.load_iris(return_X_y=True)
    for i in range(1, len(X)):
        print(f"Y Pred {i}:", model.predict([X[i]])[0], f"Y True: {y[i]}")
