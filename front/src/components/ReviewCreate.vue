
<template>
  <div>
    <h1>ReviewCreate</h1>
    <form @submit.prevent="createReview">
      <div>
        <label for="movie_title_search">Movie title search</label>
        <input v-model="query" @input="searchMovies" placeholder="Search for a movie" id="movie_title_search" name="movie_title_search"/>
        <ul v-if="movies.length">
          <li v-for="movie in movies" :key="movie.id" class="search-result__card" @click="selectMovie(movie.title, movie.poster_path)">
            <img class="img" :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="...">
            {{ movie.title }}
          </li>
        </ul>
      </div>

      <div>
        <!-- <label for="movie_title">Movie title : </label> -->
        <input type="hidden" id="movie_title" name="movie_title" v-model="movie_title">
      </div>

      <div>
        <label for="title">title : </label>
        <input type="text" id="title" name="title" v-model="title">
      </div>

      <div>
        <label for="content">content : </label>
        <textarea name="content" id="content" cols="30" rows="10" v-model="content"></textarea>
      </div>

      <!-- <div>
        <label for="rank">Rank</label>
        <input type="number" id="rank" name="rank" min="1" max="5" v-model="rank">
      </div> -->

      <div>
        <label for="rank">Rank:</label>
        <StarRating v-model="rank" />
      </div>

      <button type="submit">create</button>
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useCommunityStore } from '@/stores/community'
  import { useUserStore } from '@/stores/user'
  import axios from 'axios'
  import StarRating from '@/components/StarRating.vue'

  // community 스토어
  const store = useCommunityStore()
  // user 스토어
  const userStore = useUserStore()

  // 리뷰 작성 필드 정보
  const title = ref(null)
  const movie_title = ref(null)
  const rank = ref(0)
  const content = ref(null)
  const poster_path = ref(null)

  // 검색 변수
  const query = ref('')
  const movies = ref([])

  // 검색 기능
  const searchMovies = async () => {
  if (query.value.length >= 2) {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/v1/search/', {
        params: {
          query: query.value
        }
      })
      movies.value = response.data.results
    } catch (error) {
      console.error('영화 정보를 가져오는 중 오류 발생:', error);
    }
    } else {
      movies.value = [];
    }
  }

  // 영화 선택
  const selectMovie = (title, path) => {
    movie_title.value = title
    query.value = title
    poster_path.value = path

    searchMovies()
  }

  // 리뷰 생성
  const createReview = function() {
    const data = {
      title: title.value,
      movie_title: movie_title.value,
      content: content.value,
      rank: rank.value,
      // user 정보는 스토어에 저장된 로그인된 유저의 id 활용
      user: userStore.userId,
      poster_path: poster_path.value,
      username: userStore.loginUsername
    }
    // console.log(data)
    store.createReview(data)
    title.value=""
    movie_title.value=""
    rank.value=0
    content.value=""
    query.value = ""
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