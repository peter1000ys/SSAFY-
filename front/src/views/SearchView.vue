
<template>
  <div>
    <h1>영화 검색</h1>
    <input v-model="query" @input="searchMovies" placeholder="Search for a movie" />
    <ul v-if="movies.length">
      <li v-for="movie in movies" :key="movie.id" class="search-result__card">
        <img class="img" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="...">
        {{ movie.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      query: '',
      movies: []
    };
  },
  methods: {
    async searchMovies() {
      if (this.query.length >= 2) {
        try {
          const response = await axios.get('https://api.themoviedb.org/3/search/movie', {
            params: {
              api_key: '958a2ba52a17b56a5320e5698bd1b258',
              query: this.query,
              language: 'ko-KR'
            }
          });
          this.movies = response.data.results;
        } catch (error) {
          console.error('Error fetching movies:', error);
        }
      } else {
        this.movies = [];
      }
    }
  }
}
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