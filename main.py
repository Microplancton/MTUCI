import wikipedia 
from typing import Optional 
from pydantic import BaseModel 
from fastapi import FastAPI, Request, status 
import uvicorn 
 
app = FastAPI() 
 
class Article(BaseModel): 
title: str 
 
# PATH запрос 
 
@app.get("/article/{title}") 
def search_by_path(request: Request, title: str): 
 
titleraw = None 
for title in title.split(): 
if title != "": 
titleraw = title 
articles = 0 
try: 
data = wikipedia.summary(titleraw, sentences=4) 
except wikipedia.exceptions.DisambiguationError as e: 
data = e.options 
 
return data, status.HTTP_200_OK 
 
# QUERY запрос 
 
"/query_search/" 
def search_by_query(query: Optional[str] = None): 
 
articles = [wikipedia.search(title) for title in query.split() if title != ""] 
data = { 
"articles": [ 
{"titles": article} 
for article in articles 
] 
} 
return data, status.HTTP_200_OK 
 
# BODY запрос 
 
"/post_search/" 
def search_by_body(article: Article): 
 
articles = 0 
try: 
data = wikipedia.summary(article, sentences=4) 
except wikipedia.exceptions.DisambiguationError as e: 
data = e.options 
 
 
return data, status.HTTP_200_OK 
 
if name == "__main__": 
uvicorn.run("main:app", host="0.0.0.0", port=8000)
