<template>
  <div class="uk-grid uk-child-width-1-3@s uk-child-width-1-4@m uk-padding" uk-grid>
    <div v-for="film in films" :key="film.id">
      <div class="uk-card uk-card-default card-container" @mouseover="hoverCard(true)" @mouseleave="hoverCard(false)">
        <div class="uk-background-blend-overlay uk-background-secondary uk-background-cover uk-height-small uk-panel uk-flex uk-flex-center uk-flex-middle" :style="{ 'background-image': 'url(' + film.poster + ')' }" v-show="isHovered">
          <div class="uk-card-body card-body">
            <h3 class="col">{{ film.title }}</h3>
            <p class="col">{{ film.description }}</p>
          </div>
        </div>
        <div class="uk-background-cover uk-height-small uk-panel uk-flex uk-flex-center uk-flex-middle" :style="{ 'background-image': 'url(' + film.poster + ')' }" v-if="!isHovered">
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
      isHovered: false
    };
  },
  methods: {
    hoverCard(status) {
      this.isHovered = status;
    }
  }
};
</script>

<style>
.card-container {
  height: 500px; /* Set the height of the card to be 100% of the viewport height */
  width: auto;
}

.uk-background-cover {
  background-size: cover; /* Make the background image cover the entire container */
  height: 100%; /* Ensure the background image covers the entire card area */
}   

.col {
  color: white;
}

.card-body {
  display: none; /* Initially hide the card body */
}

.card-container:hover .card-body {
  display: block; /* Display the card body when hovering over the card container */
}
</style>
