from pydantic import BaseModel

class Film(BaseModel):
    title : str
    year : int
    date_last_watched : str
