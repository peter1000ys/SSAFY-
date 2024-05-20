
<template>
  <div>
    <div>
      <img class="img" :src="`https://image.tmdb.org/t/p/w500${review.poster_path}`" alt="...">
      <span @click.prevent="goDetail"> 영화 제목 : {{review.movie_title}} | 리뷰 내용 : {{review.content}} | 평점 : {{review.rank}}점 | </span>
      <RouterLink :to="{name:'reviewDetail', params:{reviewId:review.id}}">리뷰 상세보기</RouterLink>
      <hr>
    </div>
  </div>
</template>

<script setup>
  import { useRouter } from 'vue-router'

  // const props = defineProps({
  //   reviews:Array
  // })

  const props = defineProps({
    review:Object
  })
  // console.log(props.review.id)

  const router = useRouter()

  const goDetail = function() {
    router.push({name:'reviewDetail', params:{reviewId:props.review.id}})
  }


</script>

<style scoped>
 .img{
  width: 100px
 }
</style>