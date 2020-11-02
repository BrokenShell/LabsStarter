from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import predict


API = FastAPI(
    title='LabsStarter',
    description="""## API Stack: `FastAPI > Docker > Heroku`
### Iris Classifier Model - Support Vector Machine
- `fastapi`
- `pydantic`
- `joblib`
- `scikit-learn`
- `pandas`
- `uvicorn`
""",
    version='0.1',
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
    # This is here for initial testing only!
    # To run locally: cd into /project and run the following:
    # $ uvicorn app.main:API --host=0.0.0.0 --port=${PORT:-5000}
    uvicorn.run(API)
