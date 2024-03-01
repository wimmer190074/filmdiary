from tmdbv3api import TMDb, Search

tmdb = TMDb()
search = Search()

tmdb.api_key = '45fcb9bb0aafa77e966eba96db763446'
base_url = "https://image.tmdb.org/t/p/"
size = "original"

title = "The Matrix"
year = 1999

search = search.movies(title, year=year)

result = search[0]
print("Title:", result.title)
print("Release Date:", result.release_date)
print("Overview:", result.overview)
print("Poster URL:", base_url + size + result.poster_path)
print()
