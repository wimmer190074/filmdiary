from pydantic import BaseModel

class Film(BaseModel):
    title : str = None
    year : int = None
    date_last_watched : str = None

class FilmUpdate(BaseModel):
    id : int
    date_last_watched : str