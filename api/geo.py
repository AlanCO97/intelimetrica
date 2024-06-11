from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from schemas.geo import GeoResponse, GeoSchema
from repositories.geo import GeoRepository
from services.geo import GeoService
from db import get_db
import logging
import sys

router = APIRouter()

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter("%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s")
stream_handler.setFormatter(log_formatter)
log.addHandler(stream_handler)

geo_repository = GeoRepository()
geo_service = GeoService(geo_repository)

@router.get("/restaurants/stadistics/", response_model=GeoResponse)
def get_restaurants_in_radius(latitude: float, longitude: float, radius: float, db: Session = Depends(get_db)):
    db_restaurant = geo_service.get_restaurants_in_radius(db, GeoSchema(lat=latitude, lng=longitude, radius=radius))
    count, avg, std = db_restaurant.one()
    log.info(f"Hay {count} cerca del punto")
    return GeoResponse(count=count, avg=avg, std=std)