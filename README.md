# `Python API Development - Comprehensive Course for Beginners`
by Sanjeev Thiyagarajan, freeCodeCamp.org

`https://www.youtube.com/watch?v=0sOvCWFmrtA`

***Last_point*** 13:04:44

## Tech Stack

* Python
* FastAPI
* Pydantic
* PostgreSQL
* SQLAlchemy

## venv

### Create Virtual Environment

`$ python -m venv venv`

### Activate venv

`$ source venv/bin/activate`

### Deactivte venv

`$ deactivate`

### Export Packages List

`$ pip freeze > requirements.txt`

### Install Package List

`$ pip install -r requirements.txt`

### helpers

`$ which python`
`$ pip list`


## Fastapi

### Run

`$ uvicorn main:app --reload`
`$ uvicorn app.main:app --reload`
`$ fastapi dev main.py`