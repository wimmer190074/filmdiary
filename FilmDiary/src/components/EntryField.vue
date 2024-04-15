<template>
  <div class="uk-padding vert uk-padding-remove-bottom">
    <div class="">
      <div class="uk-grid" uk-grid>
        <div><input class="uk-input uk-form-width-medium uk-form-blank" id="film-title" type="text" placeholder="Film Name?" v-model="currentFilm"></div>
        <div><input class="uk-input uk-form-width-medium uk-form-blank uk-margin-right" id="entry-date" placeholder="Last watched?" type="text" v-model="selectedDate"></div>
        <ul class="uk-iconnav">
          <li class="icon"> <a href="#" uk-icon="icon: plus" @click="updateFilm"></a> </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script lang="ts">

export default {
  name: 'EntryField',
  data() {
    return {
      currentFilm: '', 
      selectedDate: ''
    };
  },
  methods: {
    async updateFilm() {
      const inputParts = this.currentFilm.split(',');
      const title = inputParts[0].trim();
      const year = inputParts[1] ? parseInt(inputParts[1].trim()) : '';
      const date_last_watched = this.selectedDate;
      console.log(this.selectedDate)

      const url = 'http://127.0.0.1:8000/film/';

      fetch('http://127.0.0.1:8000/film/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'accept': 'application/json'
        },
        body: JSON.stringify({
          "title": title,
          "year": year,
          "date_last_watched": date_last_watched
        })
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log(data);
        document.getElementById('film-title').value = '';
        document.getElementById('entry-date').value = '';
      })
      .catch(error => {
        console.error('There was a problem with your fetch operation:', error);
      });
    }
  }
}
</script>

<style>

.vert {
  display: flex;
  justify-content: center; /* Horizontal centering */
}

.icon {
  display: flex;
  align-items: center; /* Vertically center the icon */
}
</style>
