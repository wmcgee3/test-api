from fastapi import FastAPI

from .schemas import RootResponse

app = FastAPI()


@app.get("/", response_model=RootResponse)
def root():
    return {"_links": {"self": {"href": "/"}, "other": {"href": "/other"}}}
