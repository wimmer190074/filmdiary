<template>
  <div>
    <button @click="fetchFilms">Get Films</button>
    <ul>
      <li v-for="film in films" :key="film.id">{{ film.title }}</li>
    </ul>
  </div>
</template>

<script lang="ts">
import axios from 'axios';

export default {
  name: 'Watched',
  data() {
    return {
      films: [] as any[]
    };
  },
  methods: {
    async fetchFilms() {
      try {
        const response = await axios.get('https://ominous-palm-tree-65rrp9pg4r93p4g-8000.app.github.dev/films/');
        this.films = response.data; // Update films array with the response data
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
