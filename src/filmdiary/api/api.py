from fastapi import FastAPI
from filmdiary import FilmDataCRUD

app = FastAPI()
db = FilmDataCRUD()

@app.post("/films/")
def create_film(title: str, year: int):
    db.create_film(title, year)
    return {"message": "Ur Mum"}
    return {"message": "Vocabulary created successfully"}