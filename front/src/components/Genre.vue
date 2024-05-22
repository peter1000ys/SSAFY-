<template>
  <div>
    <h2 class="genre-title">{{ genreName }}</h2>
    <div class="movie-card-container">
      <div v-for="movie in paginatedStoreMovies" :key="movie.id" class="movie-card">
        <GenreMovieCard :movie="movie" />
      </div>
    </div>
    <div class="pagination">
      <button @click="prevPage" :disabled="currentPage === 1">이전</button>
      <span>{{ currentPage }} / {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">다음</button>
    </div>
  </div>
</template>

<script setup>
import GenreMovieCard from '@/components/GenreMovieCard.vue';
import { onMounted, ref, watch, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movie';

const route = useRoute();
const genreId = ref(route.params.genreId);
const store = useMovieStore();
const genreName = ref('');
const currentPage = ref(1);
const itemsPerPage = 10;

watch(() => route.params.genreId, (newId) => {
  genreId.value = newId;
  currentPage.value = 1; // Reset to the first page when genre changes
  fetchMovies();
  updateGenreName();
});

const fetchMovies = () => {
  store.filterMovie(genreId.value);
};

const updateGenreName = () => {
  const genre = store.genres.find(g => g.tmdb_id === Number(genreId.value));
  genreName.value = genre ? genre.name : 'Unknown';
};

const paginatedStoreMovies = computed(() => {
  const movies = store.filteredMovies || []; // Ensure movies is an array
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return movies.slice(start, end);
});

const totalPages = computed(() => {
  const movies = store.filteredMovies || []; // Ensure movies is an array
  return Math.ceil(movies.length / itemsPerPage);
});

const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--;
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++;
};

onMounted(() => {
  fetchMovies();
  updateGenreName();
});
</script>

<style scoped>
.genre-title {
  color: white;
  margin-left: 200px;
}
.movie-card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px; /* 카드 간격을 조정합니다 */
}

.movie-card {
  height: 200px;
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

.img {
  width: 100px;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  margin-top: 20px;
}
</style>
