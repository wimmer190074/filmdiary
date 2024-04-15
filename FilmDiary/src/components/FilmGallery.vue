<template>
    <div class="uk-grid uk-child-width-1-3@s uk-child-width-1-4@m uk-padding" uk-grid>
      <div v-for="film in films" :key="film.id">
        <div class="uk-card uk-card-default card-container" @mouseover="hoverCard(film.id, true)" @mouseleave="hoverCard(film.id, false)">
          <div class="uk-background-blend-overlay uk-background-secondary uk-background-cover uk-height-small uk-panel uk-flex uk-flex-center uk-flex-middle" :style="{ 'background-image': 'url(' + film.poster + ')' }" v-show="isHovered === film.id">
            <div class="uk-card-body card-body">
              <h3 class="col">{{ film.title }}</h3>
              <p class="col">{{ film.description }}</p>
              <div class="uk-card-badge uk-label" v-if="film.date_last_watched">
                <p class="col2">{{ film.date_last_watched }}</p>
              </div>
            </div>
          </div>
          <div class="uk-background-cover uk-height-small uk-panel uk-flex uk-flex-center uk-flex-middle" :style="{ 'background-image': 'url(' + film.poster + ')' }" v-if="isHovered !== film.id">
            <div class="uk-card-body card-body">
                <h3 class="col">{{ film.title }}</h3>
                <p class="col">{{ film.description }}</p>
            </div>
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
    },
    data() {
      return {
        isHovered: {}
      };
    },
    methods: {
    hoverCard(id, status) {
        if (status) {
            this.isHovered = id;
        } else {
            this.isHovered = null; // or any value that indicates no film is hovered
        }
    }
}
  };
  </script>
  
  <style>
  .card-container {
    height: 500px;
    width: auto;
  }
  
  .uk-background-cover {
    background-size: cover;
    height: 100%;
  }   
  
  .col {
    color: white;
  }

  .col2 {
    color: black
  }
  
  .card-body {
    display: none;
  }
  
  .card-container:hover .card-body {
    display: block;
  }

  .uk-card-badge {
    background-color: white;
  }
  </style>
  