<template>
  <div>
    <NavBar></NavBar>
    <FilmGallery :films="films"></FilmGallery>
  </div>
</template>

<script lang="ts">
import axios from 'axios';
import NavBar from "../components/Navbar.vue";
import FilmGallery from "../components/FilmGallery.vue";

export default {
  name: 'Watched',
  data() {
    return {
      films: [] as any[]
    };
  },
  components: {
    NavBar,
    FilmGallery
  },
  created() {
    this.fetchFilms();
  },
  methods: {
    async fetchFilms() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/films/');
        this.films = response.data.map((film: any) => ({
          ...film,
        }));
      } catch (error) {
        console.error('Error fetching films:', error);
      }
    }
  }
};
</script>

<style>
/* Add your component-specific styles here */
</style>
