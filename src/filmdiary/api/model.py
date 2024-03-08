"""This is the database model for the diary Database."""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class FilmData(Base):
    """This is the database model for the diary Database."""
    __tablename__ = 'filmdata'

    id = Column(Integer, primary_key=True)
    film_title = Column(String)
    film_year = Column(Integer)
    api_id = Column(String)
    date_last_watched = Column(DateTime)
