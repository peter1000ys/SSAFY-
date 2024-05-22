<template>
  <div class="cover-container">
    <img
      class="img"
      :src="`https://image.tmdb.org/t/p/w1280${favoriteMovies[0].backdrop_path}`"
      alt="..."
    />
    <div class="gradient-overlay"></div>
  </div>
</template>

<script setup>
defineProps({
  favoriteMovies: Array,
});
</script>

<style scoped>
.cover-container {
  width: 100%; /* 컨테이너의 너비를 100%로 설정 */
  height: 30vh; /* 컨테이너의 높이를 뷰포트 높이의 50%로 설정 */
  overflow: hidden; /* 컨테이너 밖의 이미지 부분 숨기기 */
  position: relative; /* 이미지 위치 조정을 위한 상대 위치 설정 */
}

.cover-container img {
  width: 100%; /* 이미지의 너비를 컨테이너에 맞춤 */
  height: auto; /* 이미지의 비율을 유지 */
  position: absolute; /* 절대 위치 설정 */
  top: 0; /* 이미지를 컨테이너의 상단에 맞춤 */
  transform: translateY(-25%);
}
.gradient-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.9) 90%,
    rgba(0, 0, 0, 1) 98%
  );
  pointer-events: none;
}
</style>
