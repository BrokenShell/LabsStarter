from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import predict


API = FastAPI(
    title='LABS28-API',
    description="""## API Tech Stack: `FastAPI > Docker > Heroku`
### Iris Classifier Model - Support Vector Machine
- `fastapi`
- `pydantic`
- `joblib`
- `scikit-learn`
- `pandas`
- `uvicorn`

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
""",
    version='0.42',
    docs_url='/',
)

# API Routes:
API.include_router(predict.router)


API.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(API)
