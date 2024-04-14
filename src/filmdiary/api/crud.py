from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from filmdiary import Base, FilmData
from filmdiary import FilmAPI

class FilmDataCRUD:
    def __init__(self):
        self.engine = create_engine('sqlite:///film_database.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def create_film(self, film_title, film_year, api_id=None, date_last_watched=None):
        session = self.Session()
        fd = FilmAPI()
        if api_id is None:
            fd.fetch_movie_by_title_year(film_title, film_year)
            film = FilmData(film_title=film_title, film_year=film_year, api_id=fd.id, date_last_watched=date_last_watched)
        if api_id is not None:
            film = FilmData(film_title=film_title, film_year=film_year, api_id=api_id, date_last_watched=date_last_watched)

        session.add(film)
        session.commit()
        session.close()

    def get_all_films(self):
        session = self.Session()
        films = session.query(FilmData).all()
        session.close()
        return films

    def get_film_by_id(self, film_id):
        session = self.Session()
        film = session.query(FilmData).filter_by(id=film_id).first()
        session.close()
        return film

    def update_film(self, film_id, new_title=None, new_year=None, new_api_id=None, new_date_last_watched=None):
        session = self.Session()
        film = session.query(FilmData).filter_by(id=film_id).first()
        if film:
            if new_title:
                film.film_title = new_title
            if new_year:
                film.film_year = new_year
            if new_api_id:
                film.api_id = new_api_id
            if new_date_last_watched:
                film.date_last_watched = new_date_last_watched
            session.commit()
        session.close()

    def delete_film(self, film_id):
        session = self.Session()
        film = session.query(FilmData).filter_by(id=film_id).first()
        if film:
            session.delete(film)
            session.commit()
        session.close()