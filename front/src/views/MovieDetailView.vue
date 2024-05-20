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
          <span v-if="store.genres.find(genre => genre.tmdb_id === genreSel.id)">
            {{ store.genres.find(genre => genre.tmdb_id === genreSel.id).name }}&nbsp;
          </span>
        </span>
      </div>
    </div>
    <div class="movie-detail-child">
      <h3>줄거리</h3>
      <p>{{ store.movie.overview }}</p>
    </div>
    <div class="d-flex justify-content-start" v-if="userStore.isLogin">
      <div style="margin-right: 30px;">
        <span>
          <i class="bi bi-hand-thumbs-up" 
           @click="likeMovie(store.movie.id)" 
           v-if="!store.liked" 
           style="font-size: 2rem; cursor: pointer;"
           ></i>
        <i class="bi bi-hand-thumbs-up-fill" 
           @click="likeMovie(store.movie.id)" 
           v-else 
           data-bs-toggle="popover" 
           data-bs-trigger="hover" 
           data-bs-placement="top" 
           :data-bs-content="`${store.likesCount}명이 좋아합니다.`"
           style="font-size: 2rem; cursor: pointer;"></i>
        </span>
      
      </div>
      <div style="margin-right: 30px;">
        <span>
          <i class="bi bi-hand-thumbs-down" 
           @click="hateMovie(store.movie.id)" 
           v-if="!store.hated" 
           style="font-size: 2rem; cursor: pointer;"
           ></i>
        <i class="bi bi-hand-thumbs-down-fill" 
           @click="hateMovie(store.movie.id)" 
           v-else 
           data-bs-toggle="popover" 
           data-bs-trigger="hover" 
           data-bs-placement="top" 
           :data-bs-content="`${store.hatesCount}명이 싫어합니다.`"
           style="font-size: 2rem; cursor: pointer;"></i>
        </span>
    </div>
    <div>
      <span>
          <i class="bi bi-plus" 
           @click="favoriteMovie(store.movie.id)" 
           v-if="!store.favorited" 
           style="font-size: 2rem; cursor: pointer;"
           ></i>
        <i class="bi bi-check-lg" 
           @click="favoriteMovie(store.movie.id)" 
           v-else 
           style="font-size: 2rem; cursor: pointer;"
           ></i>
        </span>
    </div>
    </div>

    <div class="d-flex justify-content-start" v-else>
      <div style="margin-right: 30px;">
        <i class="bi bi-hand-thumbs-up"  @click="loginAlert" style="font-size: 2rem; cursor: pointer;"></i>
      </div>
      <div style="margin-right: 30px;">
        <i class="bi bi-hand-thumbs-down" @click="loginAlert" style="font-size: 2rem; cursor: pointer;"></i>
      </div>
      <i class="bi bi-plus"  @click="loginAlert" style="font-size: 2rem; cursor: pointer;"></i>
    </div>
    <div class="movie-detail-child">
      <h3>공식 예고편</h3>
      <i class="bi bi-youtube" 
       data-bs-toggle="modal" 
       data-bs-target="#exampleModal"
       style="font-size: 5rem; color: #d03939; cursor: pointer;"></i>
    </div>
  </div>

</template>

<script setup>
import axios from 'axios'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
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
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@100;400;800&display=swap");

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
