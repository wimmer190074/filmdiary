from sqlalchemy import create_engine
import logging
from sqlalchemy.orm import sessionmaker
from filmdiary import Base, FilmData
from datetime import datetime

class FilmDataCRUD:
    def __init__(self):
        logging.getLogger().setLevel(logging.CRITICAL)
        self.engine = create_engine('sqlite:///film_database.db', echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)

    def create_film(self, film_title, film_year, api_id):
        film = FilmData(film_title=film_title, film_year=film_year, api_id=api_id)
        self.session.add(film)
        self.session.commit()
        return film

    def get_all_films(self):
        return self.session.query(FilmData).all()

    def get_film_by_id(self, film_id):
        return self.session.query(FilmData).filter_by(id=film_id).first()

    def update_film(self, film_id, film_title=None, film_year=None, api_id=None):
        film = self.get_film_by_id(film_id)
        if film:
            if film_title:
                film.film_title = film_title
            if film_year:
                film.film_year = film_year
            if api_id:
                film.api_id = api_id
            self.session.commit()
            return film
        return None

    def delete_film(self, film_id):
        film = self.get_film_by_id(film_id)
        if film:
            self.session.delete(film)
            self.session.commit()
            return True
        return False