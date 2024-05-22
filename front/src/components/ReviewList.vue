
<template>
  <div>
    <h1>Review List</h1>
    <div v-for="review in store.reviews" :key="review.id">
      <!-- {{ review }} -->
      <!-- <p> 작성자 : {{ review.username }} | 리뷰 내용 : {{ review.content }} | 리뷰 평점 : {{ review.rank }} | 좋아요 : {{ review.like_users.length ? review.like_users.length:0 }}명 | 싫어요 :{{ review.hate_users.length ? review.hate_user.length:0 }}명</p> -->
    {{ review }}
    </div>
  </div>
</template>

<script setup>
  import { useCommunityStore } from '@/stores/community'

  const store = useCommunityStore()

</script>

<style scoped>

</style>