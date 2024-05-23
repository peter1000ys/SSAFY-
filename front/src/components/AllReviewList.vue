<template>
  <div>
    <div id="box">
      <img
        class="img me-3"
        :src="`https://image.tmdb.org/t/p/w500${review.poster_path}`"
        alt="..."
      />
      <div class="overlay text-white">
        <p class="fs-3">{{ review.movie_title }}</p>
        <p class="fs-5">리뷰 : {{ review.content }}</p>
        <p class="fs-5"><i class="bi bi-star-fill star"></i> {{ review.rank }} </p>
        <RouterLink
          :to="{ name: 'reviewDetail', params: { reviewId: review.id } }"
          class="main-text btn btn-outline-danger mb-5"
          >
          리뷰 상세보기
        </RouterLink
        >
      </div>
    </div>
  </div>


  
</template>

<script setup>
const props = defineProps({
  review: Object,
});


</script>

<style scoped>
.img {
  width: 100px;
}
.head-main-text {
  font-size: 40px;
  font-weight: 900;
}
.main-text {
  font-size: 20px;
  font-weight: 900;
}

.card {
  background: black;
  border-radius: 2px;
  height: auto;
  margin: 1rem;
  position: relative;
  width: auto;
}

.card-1 {
  box-shadow: 0 10px 10px rgba(15, 15, 15, 0.25),
    0 10px 10px rgba(0, 0, 0, 0.22);
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.card-1:hover {
  box-shadow: 0 14px 28px rgba(22, 22, 22, 0.25),
    0 10px 10px rgba(14, 14, 14, 0.22);
}

/* 아래부터 */

#box {
  width: 300px;
  height: 500px;
  border-radius: 8px;
  overflow: hidden;
  margin: 100px auto;
  transition: all 0.3s cubic-bezier(0.42, 0.0, 0.58, 1.0);
}

#box:hover {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
  transform: translateY(-10px);
}
#box * {
  padding: 0 5px;
}

#box .img {
  display: block;
  width: inherit;
  height: inherit;;
  padding: 0;

}
#box .heading {
  font-size: 28px;
  color: white;
}

#box .data {
  display: flex;
  flex-direction: column;
  font-size: 12px;
  color: #666;
}

#box .data span {
  padding: 0;
}

#box .data .date {
  margin-bottom: 2px;
}

#box .data .user-id {
  font-size: 16px;
  color: #000;
  font-weight: 600;
}

#box .texts {
  font-size: 14px;
  line-height: 18px;
}

.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: inherit;
  height: inherit;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  background: rgb(0, 0, 0, 0.5);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s;
}

#box:hover .overlay {
  opacity: 1;
  pointer-events: auto;
}

.star {
  color: yellow;
}
</style>
