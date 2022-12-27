import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import HTTPException(HTTPException)


app = FastAPI()  # global object

db = [
    {"id": 1, "size": "s", "fuel": "gasoline", "doors": 3, "transmission": "auto"},
    {"id": 2, "size": "l", "fuel": "electric", "doors": 3, "transmission": "auto"},
    {"id": 3, "size": "m", "fuel": "gasoline", "doors": 5, "transmission": "manual"},
    {"id": 4, "size": "s", "fuel": "electric", "doors": 3, "transmission": "auto"},
    {"id": 5, "size": "l", "fuel": "hybrid", "doors": 5, "transmission": "auto"},
    {"id": 6, "size": "m", "fuel": "gasoline", "doors": 5, "transmission": "manual"},
    {"id": 7, "size": "xl", "fuel": "diesel", "doors": 5, "transmission": "manual"},
    {"id": 8, "size": "xl", "fuel": "electric", "doors": 5, "transmission": "auto"},
    {"id": 9, "size": "xl", "fuel": "hybrid", "doors": 5, "transmission": "auto"},
]

# root path
@app.get("/")  # this decorator creates a path
def read_root():
    return {"hello": "world"}

# # get all cars
# @app.get("/api/cars")
# def get_cars():
#     return db

@app.get('/api/cars')
def get_cars_by_size(size:str|None =None, doors:int|None = None)->list:
    """given a size will ouput all the cars of that size
        API query style (NOT API path parameter style)
    use : curl -X 'GET' 'http://127.0.0.1:8000/api/cars?size=s&doors=3'
    """
    result=db
    if size:
        result=[car for car in result if car['size']==size]
    if doors:
        result=[car for car in result if car['doors']>=doors]
    return result

#alternative approach using path parameters
@app.get('/api/cars/{id}')
def get_cars_by_id(id:int)->dict:
    """get cars by id using path parameter approach; the earlier approach was query parameter"""
    result=[car for car in db if car['id']==id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404,detail=f'No car with detail {id}')

# Refresher : https://app.pluralsight.com/course-player?clipId=c2a494d5-616a-4cbf-982a-217498a0e8be

# now course_id can be used in function parameter
@app.get("/course/{course_id}")
def my_course(course_id: int):
    return {"course_id": course_id}


dummy_data = [i for i in range(100)]


@app.get("/my/page/items/")
async def read_item(page: int = 0, limit: int = 0, skip: int = 1):
    return dummy_data[page * 10 : page * 10 + limit : skip]


class MyItem(BaseModel):
    name: str
    info: str = None
    price: float
    qty: int


@app.post("/purchase/item/")
async def create_item(item: MyItem):
    return {"amount": item.qty * 100, "success": True}


if __name__=='__main__':
    uvicorn.run('main:app',reload=True)
