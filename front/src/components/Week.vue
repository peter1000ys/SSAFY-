
<template>
  <div class="movie-card-container">
            <div v-for="movie in store.weekMovies" :key="movie.id">
              <WeekMovieCard :movie="movie"/>
            </div>
          </div>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue';
  import { useRecommendStore } from '@/stores/recommend';
  import WeekMovieCard from '@/components/WeekMovieCard.vue'
  
  const store = useRecommendStore()
  
    onMounted(() => {
      store.getWeekMovies()

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