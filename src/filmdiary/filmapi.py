from tmdbv3api import TMDb, Search, Movie

class FilmAPI:
    """This class uses the library tmdbv3api to load movie metadata."""
    def __init__(self):
        self.title = None
        self.year = None
        self.release_date = None
        self.overview = None
        self.poster_url = None
        self.id = None
        self.tmdb = TMDb()
        self.search = Search()
        self.movie = Movie()
        self.tmdb.api_key = '45fcb9bb0aafa77e966eba96db763446'
        self.base_url = "https://image.tmdb.org/t/p/"
        self.size = "original"

    def _fetch_movie_info(self):
        search_result = self.search.movies(self.title, year=self.year)
        if search_result:
            movie = search_result[0]
            self.title = movie.title
            self.release_date = movie.release_date
            self.overview = movie.overview
            self.poster_url = self.base_url + self.size + movie.poster_path
            self.id = movie.id
        else:
            self.title = None
            self.release_date = None
            self.overview = None
            self.poster_url = None
            self.id = None

    def fetch_movie_by_title_year(self, title, year):
        self.title = title
        self.year = year
        self._fetch_movie_info()

    def fetch_movie_by_id(self, api_id):
        film = self.movie.details(api_id)
        self.title = film.title
        self.release_date = film.release_date
        self.overview = film.overview
        self.poster_url = self.base_url + self.size + film.poster_path
        self.id = film.id

if __name__ == "__main__":
    film_api = FilmAPI()
    film_api.fetch_movie_by_id(157336)
    print("Title:", film_api.title)
    print("Release Date:", film_api.release_date)
    print("Overview:", film_api.overview)
    print("Poster URL:", film_api.poster_url)
    print("ID:", film_api.id)
