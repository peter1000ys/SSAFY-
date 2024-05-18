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
    <div>
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
    <div class="movie-detail-child">
      <h3>공식 예고편</h3>
      <button data-bs-toggle="modal" data-bs-target="#exampleModal">
      </button>
    </div>
  </div>

</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useMovieStore } from '@/stores/movie'
import YoutubeTrailerModal from '@/components/YoutubeTrailerModal.vue'

const store = useMovieStore()
const likeMovie = (movieId) => {
  store.likeMovie(movieId)
    }

    const hateMovie = (movieId) => {
      store.hateMovie(movieId)
    }

    const favoriteMovie = (movieId) => {
      store.favoriteMovie(movieId)
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

.youtube-button { 
background: red;
border-radius: 50% / 10%;
color: #FFFFFF;
font-size: 2em; 
height: 3em;
margin: 20px auto;
padding: 0;
position: relative;
text-align: center;
text-indent: 0.1em;
transition: all 150ms ease-out;
width: 4em;
}

.youtube-button::before { 
background: inherit;
border-radius: 5% / 50%;
bottom: 9%;
content: "";
left: -5%;
position: absolute;
right: -5%;
top: 9%;
}

.youtube-button::after {
border-style: solid;
border-width: 1em 0 1em 1.732em;
border-color: transparent transparent transparent rgba(255, 255, 255, 0.75);
content: ' ';
font-size: 0.75em;
height: 0;
margin: -1em 0 0 -0.75em;
top: 50%;
position: absolute;
width: 0;
}
</style>