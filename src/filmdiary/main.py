"""Sample use of the filmapi and the database."""

from filmdiary import FilmAPI
from filmdiary import FilmDataCRUD



# CRUD TEST

crud = FilmDataCRUD()

crud.create_film("Dune", 2010)
