
<template>
  <div>
    <h1>ReviewDetailView</h1>
    <div>
      <p>번호 : {{ review.id }}</p>
      <p>영화 제목 : {{ review.movie_title }}</p>
      <p>리뷰 제목 : {{ review.title }}</p>
      <p>리뷰 내용 : {{ review.content }}</p>
      <!-- <p>작성 시간 : {{ review.created_at.substr(0, 10) }} {{ review.created_at.substr(11, 8) }}</p> -->
      <p>작성자 : {{ review.user }}</p>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import { useUserStore } from '@/stores/user'
  import axios from 'axios'

  const store = useUserStore()
  const route = useRoute()
  const reviewId = ref(route.params.reviewId)
  const review = ref({})

  // 리뷰 상세 정보 요청
  onMounted(() => {
    axios({
      method: "get",
      url: `http://127.0.0.1:8000/api/v1_1/${reviewId.value}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    }).then((response) => {
      console.log(response);
      review.value = response.data
    });
  })
</script>

<style scoped>

</style>