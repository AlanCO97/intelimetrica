from fastapi import FastAPI
from api import restaurants, geo
from db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(restaurants.router, prefix="/api")
app.include_router(geo.router, prefix="/api")