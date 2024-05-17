
<template>
  <div>
    <div id="box">
    <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" class="img" alt="...">
    <h1 class="heading">{{ movie.title }}</h1>
    <div class="data">
      <span class="date">{{movie.release_date}}</span>
      <!-- <span class="user-id">{{ movie.overview }}</span> -->
    </div>
    <p class="texts">
      Lorem ipsum dolor sit amet consectetur adipisicing elit.
    </p>
  </div>
  </div>
</template>

<script setup>
  defineProps({
    movie: Object
})


</script>

<style scoped>
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
  width: 100%;
  height: 60%;
  padding: 0;

}
#box .heading {
  font-size: 28px;
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
</style>