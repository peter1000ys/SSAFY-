
<template>
  <div>
    <h1>Genre : {{ genreName }}</h1>
    <div class="movie-card-container">
      <div v-for="movie in store.filteredMovies" :key="movie.id">
              <GenreMovieCard :movie="movie" />
            </div>

    </div>
  </div>
</template>

<script setup>
import GenreMovieCard from '@/components/GenreMovieCard.vue';
import { onMounted, ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
const route = useRoute()
const GenreId = ref(route.params.genreId)
const store = useMovieStore()
const genreName = ref('');

watch(() => route.params.genreId, (newId) => {
  GenreId.value = newId;
  fetchMovies();
  updateGenreName();
});

const fetchMovies = () => {
  store.filterMovie(GenreId.value);
};
const updateGenreName = () => {
  const genre = store.genres.find(g => g.tmdb_id === Number(GenreId.value));
  genreName.value = genre ? genre.name : 'Unknown';
};

fetchMovies();
updateGenreName();
</script>

<style scoped>
.movie-card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px; /* 카드 간격을 조정합니다 */
}

.movie-card {
  flex: 1 1 calc(16.666% - 20px); /* 6개의 열을 기본으로 합니다 */
  max-width: calc(16.666% - 20px); /* 6개의 열을 기본으로 합니다 */
  margin: 10px; /* 카드 간격을 조정합니다 */
}

@media (max-width: 1200px) {
  .movie-card {
    flex: 1 1 calc(25% - 20px); /* 4개의 열로 조정 */
    max-width: calc(25% - 20px);
  }
}

@media (max-width: 768px) {
  .movie-card {
    flex: 1 1 calc(33.333% - 20px); /* 3개의 열로 조정 */
    max-width: calc(33.333% - 20px);
  }
}

@media (max-width: 480px) {
  .movie-card {
    flex: 1 1 calc(50% - 20px); /* 2개의 열로 조정 */
    max-width: calc(50% - 20px);
  }
}
</style>