from tmdbv3api import TMDb, Search

class FilmAPI:
    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.tmdb = TMDb()
        self.search = Search()
        self.tmdb.api_key = '45fcb9bb0aafa77e966eba96db763446'
        self.base_url = "https://image.tmdb.org/t/p/"
        self.size = "original"
        self._fetch_movie_info()

    def _fetch_movie_info(self):
        search_result = self.search.movies(self.title, year=self.year)
        if search_result:
            movie = search_result[0]
            self.title = movie.title
            self.release_date = movie.release_date
            self.overview = movie.overview
            self.poster_url = self.base_url + self.size + movie.poster_path
        else:
            self.title = None
            self.release_date = None
            self.overview = None
            self.poster_url = None
