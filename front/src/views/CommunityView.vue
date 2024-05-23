<template>
  <div class="font container">
    <h1>Community</h1>
    <br />
    <RouterView />
    <div class="d-flex justify-content-between">
      <h3 class="font">리뷰 목록</h3>
      <RouterLink
        :to="{ name: 'create' }"
        class="main-text btn btn-outline-danger main-text"
      >
        리뷰 작성하기
      </RouterLink>
    </div>
    <hr class="border border-danger border-2 opacity-50" />
    <div class="movie-card-container">
      <AllReviewList
        v-for="review in store.reviews"
        :key="review.id"
        :review="review"
        class="movie-card"
      />
    </div>
    <hr class="border border-danger border-2 opacity-50" />
  </div>
</template>

<script setup>
import AllReviewList from "@/components/AllReviewList.vue";
import { onMounted } from "vue";
import { useCommunityStore } from "@/stores/community";

const store = useCommunityStore();

onMounted(() => {
  store.getReviews();
});
</script>

<style scoped>
.movie-card-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px; /* 카드 간격을 조정합니다 */
}

.movie-card {
  flex: 1 1 calc(16.666% - 20px); /* 6개의 열을 기본으로 합니다 */
  max-width: calc(16.666% - 20px); /* 6개의 열을 기본으로 합니다 */
  margin: 10px; /* 카드 간격을 조정합니다 */
}

@media (max-width: 1200px) {
  .movie-card {
    flex: 1 1 calc(25% - 20px); /* 4개의 열로 조정 */
    max-width: calc(25% - 20px);
  }
}

@media (max-width: 768px) {
  .movie-card {
    flex: 1 1 calc(33.333% - 20px); /* 3개의 열로 조정 */
    max-width: calc(33.333% - 20px);
  }
}

@media (max-width: 480px) {
  .movie-card {
    flex: 1 1 calc(50% - 20px); /* 2개의 열로 조정 */
    max-width: calc(50% - 20px);
  }
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  margin-top: 20px;
}

.main-text {
  font-size: 20px;
  font-weight: 900;
}
</style>

