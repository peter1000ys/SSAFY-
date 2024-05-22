
<template>
  <div>
    <h1>related</h1>
    <div class="movie-card-container">
      <div v-for="movie in store.similarMovies" :key="movie.id">
              <RelatedMovieCard :movie="movie" />
      </div>

    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useMovieStore } from '@/stores/movie';
import RelatedMovieCard from './RelatedMovieCard.vue';
import { useRoute } from 'vue-router';

const route = useRoute()
const store = useMovieStore()
onMounted(() =>{
  store.movieDetail(route.params.movieId)
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