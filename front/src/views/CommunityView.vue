<template>
  <div>
    <h1>CommunityView</h1>
    <!-- <AllReviewList :reviews="reviews"/> -->
    <br>
    <h3>All Review List </h3>
    <AllReviewList v-for="review in reviews" :key="review.id" :review="review"/>
    <RouterLink :to="{ name: 'create'}">리뷰 작성하기</RouterLink>
  </div>
  <RouterView />
</template>

<script setup>
  import AllReviewList from '@/components/AllReviewList.vue'
  import { onMounted, ref, watch, computed, onUpdated } from 'vue'
  import { useCommunityStore } from '@/stores/community'
  import { useRouter } from 'vue-router'

  const store = useCommunityStore()
  const router = useRouter()
  const reviews = ref([])
  watch(store.reviews, (newReviews) => {
    reviews.value = newReviews
  })
  // const reviews = computed(() => store.reviews)

  onMounted(() => {
    store.getReviews()
    reviews.value = store.reviews
  })

</script>

<style scoped>
</style>