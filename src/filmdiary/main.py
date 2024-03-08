"""Sample use of the filmapi."""

from filmdiary import FilmAPI


movie_name = "The Matrix"
movie_year = 1999

returned_object = FilmAPI(movie_name, movie_year)
print(returned_object.title)
print(returned_object.release_date)
print(returned_object.overview)
print(returned_object.poster_url)
