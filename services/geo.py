from schemas.geo import GeoSchema
from repositories.geo import GeoRepository
from sqlalchemy.orm import Session

class GeoService:
    def __init__(self, geo_repository: GeoRepository) -> None:
        self.geo_repository = geo_repository
    
    def get_restaurants_in_radius(self, db: Session, geo: GeoSchema):
        return self.geo_repository.get_restaurants_in_radius(db, geo)