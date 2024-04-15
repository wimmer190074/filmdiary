<template>
  <NavBar></NavBar>
  <EntryField></EntryField>
</template>

<script lang="ts">
import EntryField from "../components/EntryField.vue";
import NavBar from "../components/Navbar.vue";

export default {
  name: 'HomeView',
  components: {
    EntryField,
    NavBar,
  },
};
</script>

<style>

</style>
