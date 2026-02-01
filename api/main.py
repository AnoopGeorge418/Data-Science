from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_post = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "title of post 2", "content": "content of post 2", "id": 2},
    {"title": "title of post 3", "content": "content of post 3", "id": 3},
]

@app.get("/")
def root(): 
    return {"message": "Welcome To My API Of Backend!"}

@app.get('/posts')
def post():
    return {"data": my_post}

@app.post('/createposts')
def post_creator(new_post: Post):
    print(new_post.rating)
    post   
    my_post.append(new_post.dict())
    return {"Data": "New Post Created"}

 

 