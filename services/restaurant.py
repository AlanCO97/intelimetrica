from schemas.restaurant import RestaurantCreate, RestaurantUpdate
from repositories.restaurant import RestaurantRepository
from sqlalchemy.orm import Session

class RestaurantService:
    def __init__(self, restaurant_repository: RestaurantRepository) -> None:
        self.restaurant_repository = restaurant_repository
    
    def create(self, db: Session, restaurant: RestaurantCreate):
        return self.restaurant_repository.create(db, restaurant)
    
    def read_all(self, db: Session):
        return self.restaurant_repository.read_all(db)
    
    def read_by_id(self, db: Session, restaurant_id: str):
        return self.restaurant_repository.read_by_id(db, restaurant_id)
    
    def update(self, db: Session, restaurant_id: str, restaurant: RestaurantUpdate):
        return self.restaurant_repository.update(db, restaurant_id, restaurant)
    
    def delete(self, db: Session, restaurant_id: str):
        return self.restaurant_repository.delete(db, restaurant_id)
        