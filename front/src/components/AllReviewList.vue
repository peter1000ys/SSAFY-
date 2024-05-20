
<template>
  <div>
    <div>
      <p @click.prevent="goDetail"> 영화 제목 : {{review.movie_title}} | 리뷰 내용 : {{review.content}} | 평점 : {{review.rank}}점</p>
      <RouterLink :to="{name:'reviewDetail', params:{reviewId:review.id}}">리뷰 상세보기</RouterLink>
      <hr>
    </div>
  </div>
  <!-- <h1>All Review List</h1> -->
  <!-- <div v-for="review in reviews" :key="review.id"> -->
  <!-- <p @click="goDetail">영화 제목 : {{ review.movie_title }} | 리뷰 : {{ review.content }} | 평점 : {{ review.rank }} 점 </p> -->
  
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

</style>