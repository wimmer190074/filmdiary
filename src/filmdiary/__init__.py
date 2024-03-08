"""init"""

from .filmapi import FilmAPI
from .api.model import FilmData, Base
from .api.crud import FilmDataCRUD

__exports__ = [
    FilmAPI,
    FilmData,
    Base, 
    FilmDataCRUD
]
