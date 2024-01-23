from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv() 

from routes.clients import routes_client
from routes.hairdressers import routes_hairdresser


app = FastAPI()
app.include_router(routes_client, prefix="/client")
app.include_router(routes_hairdresser, prefix="/hairdresser")
