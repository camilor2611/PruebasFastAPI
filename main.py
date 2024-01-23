from typing import Union
from fastapi import FastAPI
from routes.clients import routes_client
from routes.hairdressers import routes_hairdresser


app = FastAPI()
app.include_router(routes_client, prefix="/client")
app.include_router(routes_hairdresser, prefix="/hairdresser")


@app.get("/common")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}