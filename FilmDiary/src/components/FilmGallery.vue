<template>
    <div class="uk-grid uk-child-width-1-3@s uk-child-width-1-4@m padtop" uk-grid>
      <div v-for="film in films" :key="film.id">
        <div class="uk-card uk-card-default">
          <div class="uk-card-media-top">
            <img :src="film.poster" width="1800" height="1000" alt="">
          </div>
          <div class="uk-card-body">
            <h3 class="uk-card-title">{{ film.title }}</h3>
            <p>{{ film.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  export default {
    props: {
      films: {
        type: Array,
        default: () => []
      }
    }
  };
  </script>
  
  <style>
  </style>
  