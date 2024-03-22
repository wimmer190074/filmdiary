<template>
  <div>
    <h1>Title: {{ title }}</h1>
    <p>Release Date: {{ releaseDate }}</p>
    <p>Overview: {{ overview }}</p>
    <img :src="posterUrl" alt="Movie Poster">
    <p>ID: {{ id }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      title: null,
      releaseDate: null,
      overview: null,
      posterUrl: null,
      id: null,
      apiKey: '45fcb9bb0aafa77e966eba96db763446',
      baseUrl: 'https://api.themoviedb.org/3',
      posterBasePath: 'https://image.tmdb.org/t/p/original'
    };
  },
  methods: {
    async fetchMovieById(apiId) {
      try {
        const response = await axios.get(`${this.baseUrl}/movie/${apiId}?api_key=${this.apiKey}`);
        const film = response.data;
        this.title = film.title;
        this.releaseDate = film.release_date;
        this.overview = film.overview;
        this.posterUrl = this.posterBasePath + film.poster_path;
        this.id = film.id;
      } catch (error) {
        console.error('Error fetching movie:', error);
      }
    }
  },
  async created() {
    await this.fetchMovieById(157336);
  }
};
</script>
