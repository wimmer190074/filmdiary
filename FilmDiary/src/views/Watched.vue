<template>
  <div>
    <NavBar></NavBar>
    <EntryField></EntryField>
    <FilmGallery :films="films"></FilmGallery>
  </div>
</template>

<script lang="ts">
import axios from 'axios';
import NavBar from "../components/Navbar.vue";
import FilmGallery from "../components/FilmGallery.vue";
import IconNav from "../components/IconNav.vue";
import EntryField from "../components/EntryField.vue";

export default {
  name: 'Watched',
  data() {
    return {
      films: [] as any[]
    };
  },
  components: {
    NavBar,
    FilmGallery,
    IconNav,
    EntryField
  },
  created() {
    this.fetchFilms(); // Initial fetch
    setInterval(this.fetchFilms, 5000); // Poll every 5 seconds (adjust as needed)
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
