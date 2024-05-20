<template>
  <div>
    <h1>오늘의 추천 영화들</h1>
    <Date />
    <Week />
    <h1>한국의 최근 인기작들</h1>
    <Korea />
  </div> 
  <!-- <div v-if="RecStore.likedGenres">
    <div v-for="genre in RecStore.likedGenres" :key="genre.id">
      <GenreRecommend :genre="genre"/>
    </div>

  </div> -->
</template>

<script setup>
import Date from '@/components/Date.vue'
import Korea from '@/components/Korea.vue';
import Week from '@/components/Week.vue'
import { useUserStore } from '@/stores/user';
import { useRecommendStore } from '@/stores/recommend';
import { onMounted } from 'vue';
import GenreRecommend from '@/components/GenreRecommend.vue'
import { useMovieStore } from '@/stores/movie';
const userStore = useUserStore()
const RecStore = useRecommendStore()
const store = useMovieStore()
onMounted(()=>{
  RecStore.get_liked_genres(userStore.userId)
  console.log(RecStore.likedGenres)
})
const movies = []
if (RecStore.likedGenres) {
  for (let genre in RecStore.likedGenres){
    store.filterMovieRecommend(genre.tmdb_id)
    movies.push(store.filteredMoviesRec)
  }
}
</script>

<style scoped>

</style>