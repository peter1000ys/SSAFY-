<template>
  <div>
    <h1>MovieListView</h1>
    <div v-for="genre in store.genres" :key="genre.tmdb_id">
      <div>
        <RouterLink :to="{ name: 'genre', params: { genreId: genre.tmdb_id } }">{{ genre.name }}</RouterLink>
      </div>
    </div>
    <div>
      <h1>영화 검색</h1>
      <input v-model="query" @input="searchMovies" placeholder="Search for a movie" />
      <div v-if="movies.length">
        <div class="movie-card-container">
          <div v-for="movie in paginatedMovies" :key="movie.id" class="movie-card" @click="MovieDetail(movie.tmdb_id)">
            <GenreMovieCard :movie="movie" />
          </div>
        </div>
        <div class="pagination">
          <button @click="prevPage" :disabled="currentPage === 1">이전</button>
          <span>{{ currentPage }} / {{ totalPages }}</span>
          <button @click="nextPage" :disabled="currentPage === totalPages">다음</button>
        </div>
      </div>
    </div>
    <div v-if="!query">
      <div v-if="!$route.params.genreId">
        <div v-if="store.movies">
          <div class="movie-card-container">
            <div v-for="movie in paginatedStoreMovies" :key="movie.id" class="movie-card">
              <GenreMovieCard :movie="movie" />
            </div>
          </div>
          <div class="pagination">
            <button @click="prevStorePage" :disabled="currentStorePage === 1">이전</button>
            <span>{{ currentStorePage }} / {{ totalStorePages }}</span>
            <button @click="nextStorePage" :disabled="currentStorePage === totalStorePages">다음</button>
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
import { onMounted, ref, computed } from 'vue';
import { RouterLink, RouterView } from 'vue-router';
import axios from 'axios';
import { useRouter } from 'vue-router'

const query = ref('');
const movies = ref([]);
const currentPage = ref(1);
const itemsPerPage = 10;

const currentStorePage = ref(1);
const itemsPerStorePage = 10;

const router = useRouter();

const MovieDetail = function(movieId) {
  console.log(movieId);
  router.push({ name: 'detail', params: { movieId: movieId } });
};

const searchMovies = async () => {
  if (query.value.length >= 1) {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/v1/search/', {
        params: {
          query: query.value
        }
      });
      movies.value = response.data.results;
      currentPage.value = 1; // Reset to first page on new search
    } catch (error) {
      console.error('영화 정보를 가져오는 중 오류 발생:', error);
    }
  } else {
    movies.value = [];
  }
};

const paginatedMovies = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return movies.value.slice(start, end);
});

const totalPages = computed(() => {
  return Math.ceil(movies.value.length / itemsPerPage);
});

const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--;
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++;
};

const store = useMovieStore();

const paginatedStoreMovies = computed(() => {
  const start = (currentStorePage.value - 1) * itemsPerStorePage;
  const end = start + itemsPerStorePage;
  return store.movies.slice(start, end);
});

const totalStorePages = computed(() => {
  return Math.ceil(store.movies.length / itemsPerStorePage);
});

const prevStorePage = () => {
  if (currentStorePage.value > 1) currentStorePage.value--;
};

const nextStorePage = () => {
  if (currentStorePage.value < totalStorePages.value) currentStorePage.value++;
};

onMounted(() => {
  store.getGenres();
  store.getMovies();
});
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
