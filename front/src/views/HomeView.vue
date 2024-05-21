<template>
<div v-if="userStore.isLogin">
  <div v-if="RecStore.userRecommendMovies.length">
    <div class="movie-card-container">
        <h3 v-if="RecStore.userRecommendMovies">{{ userStore.loginUsername }} 님! 이런 영화는 어떠신가요?</h3>
        <div v-for="movie in RecStore.userRecommendMovies" :key="movie.id">
          <div id="box" @click="MovieDetail(movie.pk)">
            <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="img" alt="...">
            <div class="overlay">
              <h1 class="heading">{{ movie.title }}</h1>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="store.favoriteMovies.length">
      <div class="movie-card-container">
          <h3>찜한 영화 목록</h3>
          <div v-for="movie in store.favoriteMovies" :key="movie.id">
            <div id="box" @click="MovieDetail(movie.tmdb_id)">
              <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="img" alt="...">
              <div class="overlay">
                <h1 class="heading">{{ movie.title }}</h1>
              </div>
            </div>
          </div>
        </div>
      </div>
</div>
  
  <div>
    <h1>오늘의 추천 영화들</h1>
    <Date />
    <h1>랜덤 추천 영화</h1>
    <Week />
    <h1>한국의 최근 인기작들</h1>
    <Korea />
    <div v-if="RecStore.likedGenres">
      <div v-for="(movies, genre) in RecStore.likedGenres" :key="genre">
        <h2>{{ genre }}</h2>
        <GenreRecommend :movies="movies"/>
      </div>
    </div>
  </div>

</template>

<script setup>
import axios from 'axios'
import Date from '@/components/Date.vue'
import Korea from '@/components/Korea.vue'
import Week from '@/components/Week.vue'
import { useMovieStore } from '@/stores/movie'
import { useUserStore } from '@/stores/user'
import { useRecommendStore } from '@/stores/recommend'
import { onMounted, ref } from 'vue'
import GenreRecommend from '@/components/GenreRecommend.vue'
import { useRouter, onBeforeRouteLeave } from 'vue-router'
const store = useMovieStore()
// const favoriteMovies = ref([])
const userStore = useUserStore()
const RecStore = useRecommendStore()
const router = useRouter()

// const userRecommendMovies = ref([])
const MovieDetail = function(movieId) {
    console.log(movieId)
    router.push({name:'detail', params: {movieId: movieId}})
  }

// const favoriteMovie = function() {
//     axios({
//         method: "get",
//         url: `http://127.0.0.1:8000/api/v1/movies/${userStore.userId}/my_favorite/`,
//         headers: {
//           Authorization: `Token ${userStore.token}`
//         }
//       }).then((response) => {

//         favoriteMovies.value = response.data
//         console.log("프로필 찜한 영화 조회")
//       })
//         .catch((error) => {
//           console.log(error)
//       })
//   }
//   const userRecommend = function() {
//     axios({
//         method: "post",
//         url: `http://127.0.0.1:8000/api/v1/movies/${userStore.userId}/user_recommend/`,
//         headers: {
//           Authorization: `Token ${userStore.token}`
//         }
//       }).then((response) => {

//         userRecommendMovies.value = response.data
//         console.log("유저 맞춤 추천")
//       })
//         .catch((error) => {
//           console.log(error)
//       })
//   }
onMounted(() => {
  RecStore.getLikedGenresWithMovies(userStore.userId)
  store.myFavoriteMovie()
  RecStore.userRecommend()
})
// onBeforeRouteLeave((to, from) =>{
//   RecStore.userRecommendMovies = []
//   store.favoriteMovies = []
// })
</script>

<style scoped>
.img {
  width: 100px;
}
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

#box {
  width: 300px;
  height: 500px;
  border-radius: 8px;
  overflow: hidden;
  margin: 100px auto;
  transition: all 0.3s cubic-bezier(0.42, 0.0, 0.58, 1.0);
}

#box:hover {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  transform: translateY(-10px);
}
#box * {
  padding: 0 5px;
}

#box .img {
  display: block;
  width: inherit;
  height: inherit;;
  padding: 0;

}
#box .heading {
  font-size: 28px;
  color: white;
}

#box .data {
  display: flex;
  flex-direction: column;
  font-size: 12px;
  color: #666;
}

#box .data span {
  padding: 0;
}

#box .data .date {
  margin-bottom: 2px;
}

#box .data .user-id {
  font-size: 16px;
  color: #000;
  font-weight: 600;
}

#box .texts {
  font-size: 14px;
  line-height: 18px;
}

.overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: inherit;
            height: inherit;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            background: rgb(0, 0, 0, 0.5);
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.2s;
	}

#box:hover .overlay {
            opacity: 1;
            pointer-events: auto;
            
 	}

</style>
