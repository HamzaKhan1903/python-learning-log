from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, this is my first API"}

@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}
@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    return {"result": a + b}