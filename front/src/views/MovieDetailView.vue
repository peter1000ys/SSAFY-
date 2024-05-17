<template>
  <div>
    <h1>MovieDetailView</h1>
    <MovieDetailInfo />
    <YoutubeTrailer />

    <RouterLink :to="{ name: 'related'}">관련 영화</RouterLink>
    <span> | </span>
    <RouterLink :to="{ name: 'review'}">리뷰 보기</RouterLink>

  </div>
  <RouterView />
</template>

<script setup>
  import MovieDetailInfo from '@/components/MovieDetailInfo.vue'
  import YoutubeTrailer from '@/components/YoutubeTrailer.vue'

</script>

<style scoped>

</style>