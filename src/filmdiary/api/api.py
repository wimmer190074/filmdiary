from fastapi import FastAPI
from filmdiary import FilmDataCRUD
from typing import List

app = FastAPI()
db = FilmDataCRUD()


@app.post("/film/")
def create_film(title: str, year: int, api_id: int = None, date_last_watched: str = None):
    db.create_film(title, year, api_id, date_last_watched)
    return {"message": "Successfully added Film."}

@app.get("/films/")
def get_films():
    films = []
    films_data = db.get_all_films()
    for film in films_data:
        films.append({
            "id": film.id,
            "title": film.film_title,
            "year": film.film_year,
            "api_id": film.api_id,
            "date_last_watched": film.date_last_watched
        })
    return films

@app.get("/film/{film_id}")
def get_film(film_id: int):
    film = db.get_film_by_id(film_id)
    if film:
        return {
            "id": film.id,
            "title": film.film_title,
            "year": film.film_year,
            "api_id": film.api_id,
            "date_last_watched": film.date_last_watched
        }
    else:
        return {"message": "Film not found."}

@app.put("/film/{film_id}")
def update_film(film_id: int, title: str, year: int, api_id: int = None, date_last_watched: str = None):
    db.update_film(film_id, title, year, api_id, date_last_watched)
    return {"message": "Film updated successfully."}

@app.delete("/film/{film_id}")
def delete_film(film_id: int):
    db.delete_film(film_id)
    return {"message": "Film deleted successfully."}