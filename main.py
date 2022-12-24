from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def read_root():
    return {'hello':'world'}

@app.get('/course/{course_id}') #now course_id can be used in function parameter
def my_course(course_id:int):
    return {'course_id':course_id}

dummy_data=[i for i in range(100)]

@app.get('/my/page/items/')
async def read_item(page: int=0, limit:int=0,skip:int=1):
    return dummy_data[page*10: page*10 + limit:skip]

from pydantic import BaseModel
class MyItem(BaseModel):
    name:str
    info:str=None
    price:float
    qty:int

@app.post('/purchase/item/')
async def create_item(item:MyItem):
    return {'amount':item.qty*100,'success':True}