from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from filmdiary import Base, FilmData

class FilmDataCRUD:
    def __init__(self):
        self.engine = create_engine('sqlite:///film_database.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def create_film(self, film_title, film_year):
        session = self.Session()
        film = FilmData(film_title=film_title, film_year=film_year)
        session.add(film)
        session.commit()
        session.close()

if __name__ == "__main__":
    crud = FilmDataCRUD()

    x = crud.create_film("Dune", 2010)
    print(x)
