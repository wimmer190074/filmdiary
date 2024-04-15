import pytest
from sqlalchemy import create_engine
from filmdiary import Base, FilmDataCRUD

@pytest.fixture
def test_engine():
    engine = create_engine('sqlite:///:memory:')
    return engine

@pytest.fixture
def crud_instance(test_engine):
    return FilmDataCRUD(test_engine)

def test_create_film_001(crud_instance):
    crud_instance.create_film("Inception", 2010)
    films = crud_instance.get_all_films()
    print(films)
    assert len(films) == 1
    assert films[0].film_title == "Inception"
    assert films[0].film_year == 2010

def test_get_all_films_002(crud_instance):
    crud_instance.create_film("Inception", 2010)
    crud_instance.create_film("Interstellar", 2014)
    films = crud_instance.get_all_films()
    assert len(films) == 2

def test_get_film_by_id_003(crud_instance):
    crud_instance.create_film("Inception", 2010)
    films = crud_instance.get_all_films()
    film_id = films[0].id
    film = crud_instance.get_film_by_id(film_id)
    assert film.film_title == "Inception"
    assert film.film_year == 2010

def test_update_film_004(crud_instance):
    crud_instance.create_film("Inception", 2010)
    films = crud_instance.get_all_films()
    film_id = films[0].id
    crud_instance.update_film(film_id, new_title="Updated Film", new_year=2023)
    updated_film = crud_instance.get_film_by_id(film_id)
    assert updated_film.film_title == "Updated Film"
    assert updated_film.film_year == 2023

def test_delete_film_005(crud_instance):
    crud_instance.create_film("Inception", 2010)
    films = crud_instance.get_all_films()
    film_id = films[0].id
    crud_instance.delete_film(film_id)
    films_after_deletion = crud_instance.get_all_films()
    assert len(films_after_deletion) == 0
