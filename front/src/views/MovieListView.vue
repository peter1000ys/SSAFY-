<template>
  <div>
    <h1>MovieListView</h1>
    <div v-for="genre in store.genres">
      <div>
        <RouterLink :to="{name: 'genre', params: { genreId: genre.tmdb_id }}">{{ genre.name }}</RouterLink>
      </div>

    </div>
    <div v-if="!$route.params.genreId">
      <div v-if="store.movies">
        <div class="movie-card-container">
          <div v-for="movie in store.movies" :key="movie.id">
            <GenreMovieCard :movie="movie" />
          </div>
        </div>
      </div>
    </div>
    <RouterView />
  </div>
</template>

<script setup>
import GenreMovieCard from '@/components/GenreMovieCard.vue';
  import { useMovieStore } from '@/stores/movie';
  import { onMounted } from 'vue';
  import { RouterLink, RouterView } from 'vue-router';

  const store = useMovieStore()

  onMounted(()=> {
    store.getGenres()
    store.getMovies()
  })
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