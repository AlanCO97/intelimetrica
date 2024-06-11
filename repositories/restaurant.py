import uuid
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from models.models import Restaurant
from schemas.restaurant import RestaurantCreate, RestaurantUpdate
class RestaurantRepository:
    def create(self, db: Session, restaurant: RestaurantCreate):
        try:
            db_restaurant = Restaurant(
                id=str(uuid.uuid4()),
                rating=restaurant.rating,
                name=restaurant.name,
                site=restaurant.site,
                email=restaurant.email,
                phone=restaurant.phone,
                street=restaurant.street,
                city=restaurant.city,
                state=restaurant.state,
                lat=restaurant.lat,
                lng=restaurant.lng
            )
            db.add(db_restaurant)
            db.commit()
            db.flush()
            db.refresh(db_restaurant)
            return db_restaurant
        except SQLAlchemyError as e:
            db.rollback()
            raise e
    
    def read_all(self, db: Session):
        try:
            result = db.query(Restaurant)
            return result.all()
        except SQLAlchemyError as e:
            raise e
    
    def read_by_id(self, db: Session, restaurant_id: str):
        try:
            result = db.query(Restaurant).filter(Restaurant.id == restaurant_id)
            return result.first()
        except SQLAlchemyError as e:
            raise e
    
    def update(self, db: Session, restaurant_id: str, restaurant: RestaurantUpdate):
        try:
            result = db.query(Restaurant).filter(Restaurant.id == restaurant_id)
            db_restaurant = result.first()
            if db_restaurant is None:
                raise ValueError("Restaurant not found")
            db_restaurant.rating = restaurant.rating
            db_restaurant.name = restaurant.name
            db_restaurant.site = restaurant.site
            db_restaurant.email = restaurant.email
            db_restaurant.phone = restaurant.phone
            db_restaurant.street = restaurant.street
            db_restaurant.city = restaurant.city
            db_restaurant.state = restaurant.state
            db_restaurant.lat = restaurant.lat
            db_restaurant.lng = restaurant.lng
            db.commit()
            db.refresh(db_restaurant)
            return db_restaurant
        except SQLAlchemyError as e:
            db.rollback()
            raise e
    
    def delete(self, db: Session, restaurant_id: str):
        try:
            result = db.query(Restaurant).filter(Restaurant.id == restaurant_id)
            db_restaurant = result.first()
            if db_restaurant is None:
                raise ValueError("Restaurant not found")
            db.delete(db_restaurant)
            db.commit()
            return db_restaurant
        except SQLAlchemyError as e:
            db.rollback()
            raise e