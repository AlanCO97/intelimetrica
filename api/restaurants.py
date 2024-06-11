from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
from schemas.restaurant import Restaurant, RestaurantCreate, RestaurantUpdate
from repositories.restaurant import RestaurantRepository
from services.restaurant import RestaurantService
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

restaurant_repository = RestaurantRepository()
restaurant_service = RestaurantService(restaurant_repository)

@router.post("/restaurants", response_model=Restaurant)
def create(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    db_restaurant = restaurant_service.create(db, restaurant)
    if db_restaurant is None:
        raise HTTPException(status_code=400, detail="not saved")
    log.info("El restaurante se ha agregado con exito")
    return db_restaurant

@router.get("/restaurants", response_model=List[Restaurant])
def read_all(db: Session = Depends(get_db)):
    log.info("Obteniendo todos los restaurantes")
    db_restaurant = restaurant_service.read_all(db)
    return db_restaurant

@router.get("/restaurants/{restaurant_id}", response_model=Restaurant)
def read_by_id(restaurant_id: str, db: Session = Depends(get_db)):
    log.info(f"Obteniendo el restaurante con id {restaurant_id}")
    db_restaurant = restaurant_service.read_by_id(db, restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="not found")
    return db_restaurant

@router.put("/restaurants/{restaurant_id}", response_model=Restaurant)
def update(restaurant_id: str, restaurant: RestaurantUpdate, db: Session = Depends(get_db)):
    try:
        log.info(f"Actualizando el restaurante con id {restaurant_id}")
        db_restaurant = restaurant_service.update(db, restaurant_id, restaurant)
        
        return db_restaurant
    except ValueError as e:
        log.info(f"No se encontro el restaurante con id {restaurant_id}, error: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))

    except Exception as e:
        log.info(f"Hubo un error al actualizar el restaurante con id {restaurant_id}, error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/restaurants/{restaurant_id}")
def delete_reservation(restaurant_id: str, db: Session = Depends(get_db)):
    try:
        log.info(f"Eliminando el restaurante con id {restaurant_id}")
        restaurant_service.delete(db, restaurant_id)
       
        return {"message": "Restaurant deleted successfully"}
    except ValueError as e:
        log.info(f"No se encontro el restaurante con id {restaurant_id}, error: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        log.info(f"Hubo un error al eliminar el restaurante con id {restaurant_id}, error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
