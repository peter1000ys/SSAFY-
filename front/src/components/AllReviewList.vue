
<template>
  <div>
    <h1>All Review List</h1>
    <div v-for="review in reviews" :key="review.id">
      <div>
        영화 제목 : {{ review.movie_title }}  리뷰 : {{ review.content }} 평점 : {{ review.rank }} 점
      </div>
      <RouterLink :to="{name:'reviewDetail', params:{reviewId:review.id}}">리뷰 상세보기</RouterLink>
      <hr>
    </div>
  </div>
</template>

<script setup>
  import { useRouter } from 'vue-router'

  defineProps({
    reviews:Array
  })


</script>

<style scoped>

</style>