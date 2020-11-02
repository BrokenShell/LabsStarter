from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import predict

API = FastAPI(
    title='LabsStarter',
    description="<h3>This is a test of `FastAPI > Docker > Heroku`</h3>",
    version='0.1',
    docs_url='/',
)

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
    # This is for initial testing Only! Use Docker.
    uvicorn.run(API)
