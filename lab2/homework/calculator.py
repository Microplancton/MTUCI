import uvicorn
from fastapi import FastAPI, Request, status
from pydantic import BaseModel

app = FastAPI()

class Article(BaseModel):
    title: str

# PATH запрос

@app.get("/from_path/{equation}")
def search_by_path(request: Request, equation: str):
    
    for equation in equation.split():
        if equation != "":
            try:
                equation = equation.replace(':', '/')
                data = eval(equation)
            except:
                data = "ошибка в математическом выражении!"
            return data, status.HTTP_200_OK
    return status.HTTP_500_INTERNAL_SERVER_ERROR
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)