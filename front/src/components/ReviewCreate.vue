
<template>
  <div>
    <h1>ReviewCreate</h1>
    <form @submit.prevent="createReview">
      <div>
        <label for="title">title : </label>
        <input type="text" id="title" name="title" v-model="title">
      </div>

      <div>
        <label for="movie_title">Movie title : </label>
        <input type="text" id="movie_title" name="movie_title" v-model="movie_title">
      </div>

      <div>
        <label for="content">content : </label>
        <textarea name="content" id="content" cols="30" rows="10" v-model="content"></textarea>
      </div>

      <div>
        <label for="rank">Rank</label>
        <input type="number" id="rank" name="rank" min="1" max="5" v-model="rank">
      </div>

      <button type="submit">create</button>
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useCommunityStore } from '@/stores/community'
  import { useUserStore } from '@/stores/user'

  // community 스토어
  const store = useCommunityStore()
  // user 스토어
  const userStore = useUserStore()

  // 리뷰 작성 필드 정보
  const title = ref(null)
  const movie_title = ref(null)
  const rank = ref(null)
  const content = ref(null)

  const createReview = function() {
    const data = {
      title: title.value,
      movie_title: movie_title.value,
      content: content.value,
      rank: rank.value,
      // user 정보는 스토어에 저장된 로그인된 유저의 id 활용
      user: userStore.userId
    }
    console.log(data)
    store.createReview(data)
  }
</script>

<style scoped>

</style>