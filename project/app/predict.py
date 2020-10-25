from fastapi import APIRouter
from joblib import load
from app.data import Iris


router = APIRouter()
model = load('app/model.joblib')


@router.post('/predict')
async def predict(iris: Iris):
    lookup = ('Setosa', 'Versicolor', 'Virginica')
    x = iris.to_df()
    y_pred, *_ = model.predict(x)
    y_prob, *_ = model.predict_proba(x)
    return {
        'prediction': lookup[y_pred],
        'confidence': f'{100 * max(y_prob):.2f}%',
    }
