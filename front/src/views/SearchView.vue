
<template>
  <div>
    <h1>영화 검색</h1>
    <input v-model="query" @input="searchMovies" placeholder="Search for a movie" />
    <ul v-if="movies.length">
      <li v-for="movie in movies" :key="movie.tmdb_id" class="search-result__card" @click="selectMovie(movie.title, movie.tmdb_id)">
        <img class="img" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="...">
        {{ movie.title }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router';

const query = ref('');
const movies = ref([]);
const router = useRouter()

const searchMovies = async () => {
  if (query.value.length >= 2) {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/v1/search/', {
        params: {
          query: query.value,
        }
      })
      movies.value = response.data.results;
    } catch (error) {
      console.error('영화 정보를 가져오는 중 오류 발생:', error);
    }
  } else {
    movies.value = [];
  }
};
const selectMovie = (title, movieId) => {
  query.value = title;
  router.push({name:'detail', params:{movieId:movieId}})
  searchMovies()
};
</script>

<style scoped>
.img{
  width: 100px;
}

.search-result__card:hover  {
  cursor: pointer;
  color: white;
  background-color: #3B82F6; 
}
</style>