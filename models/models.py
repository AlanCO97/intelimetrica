from sqlalchemy import Column, Integer, Text, Float
from db import Base

class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Text, primary_key=True)
    rating = Column(Integer)
    name = Column(Text)
    site = Column(Text)
    email = Column(Text)
    phone = Column(Text)
    street = Column(Text)
    city = Column(Text)
    state = Column(Text)
    lat = Column(Float)
    lng = Column(Float)