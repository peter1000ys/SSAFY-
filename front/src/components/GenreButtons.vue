<template>
  <div class="genres">
    <div v-for="genre in genres" :key="genre.tmdb_id">
      <div>
        <button
          type="button"
          class="btn btn-outline-danger"
          :class="{ active: selectedGenreId === genre.tmdb_id }"
          @click="onGenreClick(genre.tmdb_id)"
        >
          {{ genre.name }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore();
const genres = store.genres;
const router = useRouter();
const selectedGenreId = ref(null);

const onGenreClick = (genreId) => {
  if (selectedGenreId.value === genreId) {
    router.push({ name: 'list'});
    selectedGenreId.value = null;
  } else {
    selectedGenreId.value = genreId;
    router.push({ name: 'genre', params: { genreId } });
  }
};

</script>

<style scoped>
button {
  width: 150px;
}
.genres {
  display: grid;
  grid-template-columns: repeat(10, 1fr); /* 12개의 열로 나누기 */
  gap: 10px;
  -ms-grid-column-align: center;
  align-items: center;
  text-align: center;
}

button.active {
  background-color: #dc3545;
  color: white;
}
</style>





