from geoalchemy2 import Geography
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from models.models import Restaurant
from schemas.geo import GeoSchema

class GeoRepository:
    def get_restaurants_in_radius(self, db: Session, geo: GeoSchema):
        try:
            result = db.query(
                func.count(Restaurant.id),
                func.coalesce(func.avg(Restaurant.rating), 0),
                func.coalesce(func.stddev(Restaurant.rating), 0)
            ).filter(
                func.ST_DWithin(
                     func.ST_MakePoint(Restaurant.lng, Restaurant.lat).cast(Geography),
                    func.ST_MakePoint(geo.lng, geo.lat).cast(Geography),
                    geo.radius
                )
            )
            return result
        except SQLAlchemyError as e:
            raise e