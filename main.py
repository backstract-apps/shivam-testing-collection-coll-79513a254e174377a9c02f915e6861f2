from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - shivam-testing-collection-coll-79513a254e174377a9c02f915e6861f2',debug=False,docs_url='/stupefied-haibt-e5d8992eb3c011ef8ebd0242ac12000282/docs',openapi_url='/stupefied-haibt-e5d8992eb3c011ef8ebd0242ac12000282/openapi.json')

app.include_router(router, prefix='/stupefied-haibt-e5d8992eb3c011ef8ebd0242ac12000282/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()