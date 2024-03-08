"""Sample use of the filmapi and the database."""

from filmdiary import FilmAPI
from filmdiary import FilmDataCRUD


# FILM API TEST

movie_name = "The Matrix"
movie_year = 1999

returned_object = FilmAPI(movie_name, movie_year)
print(returned_object.id)
print(returned_object.title)
print(returned_object.release_date)
print(returned_object.overview)
print(returned_object.poster_url)


# CRUD TEST

crud = FilmDataCRUD()

all_films = crud.get_all_films()
for film in all_films:
    print(film.film_title)
