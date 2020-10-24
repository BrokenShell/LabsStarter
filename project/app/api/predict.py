import logging

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator
from joblib import load


log = logging.getLogger(__name__)
router = APIRouter()
model = load('model/clf.joblib')


class Iris(BaseModel):
    sepal_length: float = Field(..., example=5.8)
    sepal_width: float = Field(..., example=2.3)
    petal_length: float = Field(..., example=3.3)
    petal_width: float = Field(..., example=1.0)

    def to_df(self):
        return pd.DataFrame([dict(self)])

    @validator('sepal_length', 'sepal_width', 'petal_length', 'petal_width')
    def must_be_positive(cls, value):
        assert value > 0, f'value == {value}, must be > 0'
        return value


@router.post('/predict')
async def predict(iris: Iris):
    lookup = ('setosa', 'versicolor', 'virginica')
    X = iris.to_df()
    log.info(X)
    y_pred = model.predict(X)
    return {
        'prediction': lookup[y_pred[0]],
    }
