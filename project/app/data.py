from pydantic import BaseModel, Field, validator
import pandas as pd


class Iris(BaseModel):
    """ Example: #55 [5.7, 2.8, 4.5, 1.3] == 1 (Versicolor) @ 92.69% """
    sepal_length: float = Field(..., example=5.7)
    sepal_width: float = Field(..., example=2.8)
    petal_length: float = Field(..., example=4.5)
    petal_width: float = Field(..., example=1.3)

    def to_df(self):
        return pd.DataFrame([dict(self)])

    @validator('sepal_length', 'sepal_width', 'petal_length', 'petal_width')
    def check_val(cls, value):
        assert 0 < value < 10, f'value == {value}, 0 < value < 10'
        return value


if __name__ == '__main__':
    iris = Iris(
        sepal_length=5.7,
        sepal_width=2.8,
        petal_length=4.5,
        petal_width=1.3,
    )
    print(iris.to_df())
