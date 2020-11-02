# Lambda LabsStarter Kit

## API Tech Stack: `FastAPI > Docker > Heroku`

To install and run with your favorite virtual environment:
```
(venv) $ pip install -r project/requirements.txt
(venv) $ cd project
(venv) project $ uvicorn app.main:API --host=0.0.0.0 --port=${PORT:-5000}
```

To build and run a local docker image:
```
$ docker build . -t hrf
$ docker run -it -p 5000:5000 hrf uvicorn app.main:API --host=0.0.0.0 --port=5000
```

To deploy, push to GitHub and use the Heroku GitHub integration tool.
- See documentation on [Heroku](https://heroku.com)


### Iris Classifier Model - Support Vector Machine
- `fastapi`
- `pydantic`
- `joblib`
- `scikit-learn`
- `pandas`
- `uvicorn`

### Scikit SVM Classification Model
- Baseline Guess Accuracy: 33.33%
- SVM Training Accuracy: 98.33%
- SVM Validation Accuracy: 96.67%

### Measurement Input:
- Sepal Length: float centimeters
- Sepal Width: float centimeters
- Petal Length: float centimeters
- Petal Width: float centimeters

### Species Name Output:
0. Setosa
1. Virginica
2. Versicolor

### Prediction Confidence Range:
0.0 - 100.0%


### Prediction Example:
```
input={
  "sepal_length": 5.7,
  "sepal_width": 2.8,
  "petal_length": 4.5,
  "petal_width": 1.3
}
```
```
output={
  "prediction": "Versicolor",
  "confidence": "92.69%"
}
```
