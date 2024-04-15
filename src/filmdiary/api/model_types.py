from pydantic import BaseModel

class Film(BaseModel):
    title : str
    year : int
