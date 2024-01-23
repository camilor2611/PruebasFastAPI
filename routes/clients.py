from fastapi import APIRouter
from schemas.client import Client, CreatedClient
from schemas.booking import CreatedBook, Book


routes_client = APIRouter()


@routes_client.post("/new-client", response_model=CreatedClient)
def new_client(req_client: Client):
    try:
        return {"isCreated": True}
    except Exception as e:
        return {"msg": str(e)}
    

@routes_client.post("/new-book", response_model=CreatedBook)
def new_book(req_book: Book):
    try:
        return {"isCreated": True}
    except Exception as e:
        return {"msg": str(e)}