from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app import predict

API = FastAPI(
    title='LabsStarter',
    description='This is just a test.',
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
    uvicorn.run(API)
