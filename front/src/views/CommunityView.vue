<template>
  <div>
    <h1>CommunityView</h1>
    <AllReviewList :reviews="reviews"/>
    <hr>
    <br>
    <RouterLink :to="{ name: 'create'}">리뷰 작성하기</RouterLink>
  </div>
  <RouterView />
</template>

<script setup>
  import AllReviewList from '@/components/AllReviewList.vue'
  import { onMounted, ref, watch } from 'vue';
  import { useCommunityStore } from '@/stores/community'

  const store = useCommunityStore()
  onMounted(() => {
    store.getReviews()
  })  
  const reviews = store.reviews

</script>

<style scoped>
</style>