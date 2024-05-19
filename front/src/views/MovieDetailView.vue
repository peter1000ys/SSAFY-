<template>
  <YoutubeTrailerModal />
  <div class="movie-detail-container">
    <img :src="`https://image.tmdb.org/t/p/w500${store.movie.poster_path}`" alt="">
    <h3>{{ store.movie.title }}</h3>
    <div class="movie-detail-child">
      <p><strong>개봉일:</strong> {{ store.movie.release_date }}</p>
      <p><strong>러닝타임:</strong> {{ store.movie.runtime }}</p>
      <p><strong>TMDB 평점:</strong> {{ store.movie.vote_average }}</p>
    </div>
    <div class="movie-detail-child">
      <h3>장르</h3>
      <div>
        <span v-for="genreSel in store.movie.genres" :key="genreSel.id">
          <p v-for="genre in store.genres">
            <p v-if="genre.tmdb_id===genreSel.id">
              {{ genre.name }}&nbsp;
            </p>
          </p>
        </span>
      </div>
    </div>
    <div class="movie-detail-child">
      <h3>줄거리</h3>
      <p>{{ store.movie.overview }}</p>
    </div>
    <div v-if="userStore.isLogin">
      <button @click="likeMovie(store.movie.id)">
        {{ store.liked ? '좋아요 취소' : '좋아요' }} ({{ store.likesCount }})
      </button>
      <button @click="hateMovie(store.movie.id)">
        {{ store.hated ? '싫어요 취소' : '싫어요' }} ({{ store.hatesCount }})
      </button>
      <button @click="favoriteMovie(store.movie.id)">
        {{ store.favorited ? '찜 취소' : '찜하기' }}
      </button>
    </div>
    <div v-else>
      <button @click="loginAlert">{{ '좋아요' }}</button>
      <button @click="loginAlert">{{ '싫어요' }}</button>
      <button @click="loginAlert">{{ '찜하기' }}</button>
    </div>
    <div class="movie-detail-child">
      <h3>공식 예고편</h3>
      <button data-bs-toggle="modal" data-bs-target="#exampleModal">
        Trailer
      </button>
    </div>
  </div>

</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useMovieStore } from '@/stores/movie'
import { useUserStore } from '@/stores/user'
import YoutubeTrailerModal from '@/components/YoutubeTrailerModal.vue'
const userStore = useUserStore()
const store = useMovieStore()
const router = useRouter()
const likeMovie = (movieId) => {
  store.likeMovie(movieId)
    }

    const hateMovie = (movieId) => {
      store.hateMovie(movieId)
    }

    const favoriteMovie = (movieId) => {
      store.favoriteMovie(movieId)
    }
const loginAlert = () => {
  window.alert('로그인이 필요합니다!')
  router.push({name: 'login'})
}
onMounted(() => {
  const route = useRoute()
  const movieId = route.params.movieId

  store.movieDetail(movieId)

})
</script>

<style scoped>
.movie-detail-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 100px;
}

.movie-detail-child {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 10px 0;
}

img {
  width: 300px;
}

</style>
