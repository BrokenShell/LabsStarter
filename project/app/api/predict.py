import logging

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator
from joblib import load

log = logging.getLogger(__name__)
router = APIRouter()
model = load('app/api/model.joblib')


class Iris(BaseModel):
    """ Example: [5.7, 2.8, 4.1, 1.3] == 1 Versicolor 98.38% """
    sepal_length: float = Field(..., example=5.7)
    sepal_width: float = Field(..., example=2.8)
    petal_length: float = Field(..., example=4.1)
    petal_width: float = Field(..., example=1.3)

    def to_df(self):
        return pd.DataFrame([dict(self)])

    @validator('sepal_length', 'sepal_width', 'petal_length', 'petal_width')
    def must_be_positive(cls, value):
        assert value > 0, f'value == {value}, must be > 0'
        return value


@router.post('/predict')
async def predict(iris: Iris):
    lookup = ('Setosa', 'Versicolor', 'Virginica')
    X = iris.to_df()
    log.info(X)
    y_pred = lookup[model.predict(X)[0]]
    y_pred_proba = f'{100 * max(model.predict_proba(X)[0]):.2f}%'
    return {
        'prediction': y_pred,
        'probability': y_pred_proba,
    }
