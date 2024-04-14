<template>
  <div>
    <div class="uk-margin">
      <input class="uk-input uk-form-width-medium" type="text" placeholder="Default" aria-label="Default" v-model="currentText" @keydown.enter="updateTextInput">
    </div>
    <div>{{ textInput }}</div>
    <div>{{ currentText }}</div>
  </div>
</template>

<script lang="ts">
export default {
  name: 'HomeView',
  data() {
    return {
      textInput: '', 
      currentText: ''
    };
  },
  methods: {
    updateTextInput(event) {
      if (event.key === 'Enter') {
        this.textInput = event.target.value;
      }
    }
  }
};
</script>

<style>
</style>
