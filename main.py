from fastapi import FastAPI

app = FastAPI(title="스터디 플랫폼 API")


@app.get("/hello")
def hello():
    return {"message": "안녕하세요! FastAPI 서버가 동작 중입니다."}


@app.get("/hello/{name}")
def hello_name(name: str):
    return {"message": f"{name}님, 환영합니다!"}


@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}
