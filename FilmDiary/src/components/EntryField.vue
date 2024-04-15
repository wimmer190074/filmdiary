<template>
  <div class="uk-padding uk-position-center">
    <div class="uk-margin">
      <input class="uk-input uk-form-width-medium" type="text" placeholder="Enter the film" aria-label="Default" v-model="currentText" @keydown.enter="updateTextInput">
      <!-- <div class="uk-card uk-card-body uk-card-default" uk-drop="animation: uk-animation-slide-top-small; animate-out: true; mode: click">{{ currentText }}</div> -->
    </div>
  </div>
</template>

<script lang="ts">

import axios from 'axios';

export default {
  name: 'EntryField',
  data() {
    return {
      textInput: '', 
      currentText: '',
    };
  },
  methods: {
    async updateTextInput(event) {
      if (event.key === 'Enter') {
          const inputParts = this.currentText.split(',');
          const title = inputParts[0].trim();
          const year = inputParts[1] ? parseInt(inputParts[1].trim()) : '';

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
          })
          .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
          });
      }
    }
  }
}
</script>

<style>
</style>