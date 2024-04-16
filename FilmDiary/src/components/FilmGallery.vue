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
              <li><a href="#" uk-icon="icon: file-edit" @click="openEditModal(film)"></a></li>
              <li><a href="#" uk-icon="icon: trash" @click="trashFilm(film.id)"></a></li>
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
    <div id="editModal" uk-modal>
      <div class="uk-modal-dialog uk-modal-body">
        <h2 class="uk-modal-title">{{ editedFilm.title }}</h2>
        <p>{{ editedFilm.description }}</p>
        <label class="uk-margin-right" for="newDate">New Last Watched Date:</label>
        <input class="uk-margin-right" type="text" id="newDate" v-model="newLastWatchedDate">
        <button class="uk-button uk-button-default" @click="saveEditedFilm()">Save</button>
        <button class="uk-modal-close-default" type="button" uk-close></button>
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
      isHovered: {},
      editedFilm: {},
      newLastWatchedDate: ''
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
    openEditModal(film) {
      this.editedFilm = film;
      UIkit.modal("#editModal").show();
      return editedFilm
    },

    hoverCard(id, status) {
      if (status) {
          this.isHovered = id;
      } else {
          this.isHovered = null; // or any value that indicates no film is hovered
      }
    },
    async editFilm(id) {
      console.log(id)
      fetch('http://127.0.0.1:8000/film/'+ id, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'accept': 'application/json'
        },
        body: JSON.stringify({
          "id": id,
          "title": "Testing",
          "year": "1234",
          "date_last_watched": "date_last_watched"
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
        this.$emit('fetch-film');
      })
      .catch(error => {
        console.error('There was a problem with your fetch operation:', error);
      });
    },
    async trashFilm(id) {
      console.log(id);
      try {
        const response = await fetch(`http://127.0.0.1:8000/film/${id}`, {
          method: 'DELETE'
        });
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        console.log('Film deleted successfully');
        this.$emit('fetch-film');
      } catch (error) {
        console.error('There was a problem with your fetch operation:', error);
      }
    },
    async saveEditedFilm() {
      const id = this.editedFilm.id;
      const newDate = this.newLastWatchedDate;
      try {
        const response = await fetch(`http://127.0.0.1:8000/film/` + id, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
            'accept': 'application/json'
          },
          body: JSON.stringify({
            "id": id,
            "title": '',
            "year": '',
            "api_id": '',
            "date_last_watched": newDate
          })
        });
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        console.log('Film updated successfully');
        this.$emit('fetch-film');
        UIkit.modal("#editModal").hide();
      } catch (error) {
        console.error('There was a problem with your fetch operation:', error);
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
