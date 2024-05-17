<template>
  <div>
    <RouterLink :to="{ name:'home'}">home</RouterLink>
    <span> | </span>
    <RouterLink :to="{ name:'list'}">list</RouterLink>
    <span> | </span>
    <!-- MovieDetailView 라우터 링크 -->
    <RouterLink :to="{ name:'detail', params: {'movieId' : movieId} }">detail</RouterLink>
  </div>
  <RouterView/>
</template>

<script setup>
  // import { RouterLink, RouterView } from 'vue-router'
  import { ref } from 'vue'
  // 컴포넌트 확인용 movieId 변수
  const movieId = ref(1)
</script>

<style scoped>

</style>
