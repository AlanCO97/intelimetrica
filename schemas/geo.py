from pydantic import BaseModel, confloat

class GeoSchema(BaseModel):
    lat: float
    lng: float
    radius: confloat(ge=0) # type: ignore

class GeoResponse(BaseModel):
    count: int
    avg: float
    std: float