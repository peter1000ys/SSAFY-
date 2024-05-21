<template>
  <div>
    <div>
      <RouterLink :to="{ name:'home'}">home</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name:'list'}">list</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name:'community'}">community</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name:'search'}">search</RouterLink>
      <!-- <span> | </span> -->
      <!-- MovieDetailView 라우터 링크 -->
      <!-- <RouterLink :to="{ name:'detail', params: {'movieId' : movieId} }">detail</RouterLink> -->
    </div>
    
    <div v-if="!store.isLogin">
      <RouterLink :to="{ name:'signup'}">회원가입</RouterLink>
      <span> | </span>
      <RouterLink :to="{ name:'login'}">로그인</RouterLink>

    </div>
    <div v-else>
      <button @click="logout">로그아웃</button>
      <span> | </span>
      <RouterLink :to="{ name:'profile'}">프로필</RouterLink>
    </div>
  </div>
  <RouterView/>
</template>

<script setup>
  import { ref } from 'vue'
  import { useUserStore } from '@/stores/user';
  import { useRouter } from 'vue-router'

  const store = useUserStore()
  const router = useRouter()

  // 컴포넌트 확인용 movieId 변수 임시 할당
  // const movieId = ref(1)

  // 로그아웃 함수
  const logout = function () {
    store.logout()
    router.push({ name: 'login'})
  }

</script>

<style scoped>

</style>
