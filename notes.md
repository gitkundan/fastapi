https://app.pluralsight.com/guides/explore-python-libraries:-fastapi
pip install fastapi[all]
uvicorn main:app --reload
always add type hints - that is used by pydantic to do data validation
type int of parameter will also coerce the argument into that data type

use multiple type hints
get_cars_by_size(size:str|None =None, doors:int|None = None)->list:

starter code

```python
from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def read_root():
    return {'hello':'world'}
```

API design:
two options: path parameters (../.../..) or query parameters (/?car=tesla)
if the url is x.x.x.x:8000/?name=reindeer
then function parameter **name** will be passed to the underlying function with argument as reindeer

**curl to get data from GET endpoint**
curl -X 'GET' 'http://127.0.0.1:8000/cars' -H 'accept: application/json'

REST API best practices : prefix with api : /api/cars and not /cars


**Pydantic model classes**
these classes are the model of the car and these models will be persisted to database
these classes will keep the correct relations



**lambda**
lamda function are JS anonymous function 
(a) for single use
(b) inline use in a single line
(c) instead of => use :
(d) cant be tested
(e) used inside another function
(f) will return at least one value i.e. no side-effect
(g) used to transform input into another function i.e. for function-of-function situations (fof)
(h) if the function is one/two lines then refactor as lambda
(i) 

 