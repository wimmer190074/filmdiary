<template>
    <div class="uk-grid uk-child-width-1-3@s uk-child-width-1-4@m uk-padding" uk-grid>
      <div v-for="film in sortedFilms" :key="film.id">
        <div class="uk-card uk-card-default card-container" @mouseover="hoverCard(film.id, true)" @mouseleave="hoverCard(film.id, false)">
          <div class="uk-background-blend-overlay uk-background-secondary uk-background-cover uk-height-small uk-panel uk-flex uk-flex-center uk-flex-middle" :style="{ 'background-image': 'url(' + film.poster + ')' }" v-show="isHovered === film.id">
            <div class="uk-card-body card-body">
              <h3 class="col">{{ film.title }}</h3>
              <p class="col">{{ film.description }}</p>
              <div class="uk-card-badge uk-label" v-if="film.date_last_watched">
                <p class="col2">Last Watched on: {{ film.date_last_watched }}</p>
              </div>
              <div class="uk-iconnav col">
                <li><a href="#" uk-icon="icon: file-edit"></a></li>
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
    computed: {
      sortedFilms() {
        return this.films.slice().sort((a, b) => {
          return new Date(b.date_last_watched) - new Date(a.date_last_watched);
        });
      }
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
    height: 60vh;
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
  