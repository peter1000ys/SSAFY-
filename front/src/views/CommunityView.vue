<template>
  <div>
    <h1>CommunityView</h1>
    <br>
    <h3>All Review List</h3>
    <AllReviewList
      v-for="review in store.reviews"
      :key="review.id"
      :review="review"
    />
    <RouterLink :to="{ name: 'create' }">리뷰 작성하기</RouterLink>
  </div>
  <RouterView />
</template>

<script setup>
import AllReviewList from "@/components/AllReviewList.vue";
import { onMounted, ref } from "vue";
import { useCommunityStore } from "@/stores/community";

const store = useCommunityStore()

onMounted(() => {
  store.getReviews()
})
</script>

<style scoped></style>
