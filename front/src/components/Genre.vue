
<template>
  <div>
    <h1>Genre</h1>
    <GenreMovieCard />
  </div>
</template>

<script setup>
  import GenreMovieCard from '@/components/GenreMovieCard.vue';
  
  defineProps({
    genre:Object
  })
</script>

<style scoped>

</style>