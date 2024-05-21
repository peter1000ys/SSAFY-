<template>
  <div class="home">
    <div class="overlay">
      <header class="header">
        <img class="logo" src="@/assets/site_logo.png">
        <div class="nav">
          <div class="nav-item"><RouterLink :to="{ name:'home'}">홈</RouterLink></div>
          <div class="nav-item"><RouterLink :to="{ name:'list'}">영화</RouterLink></div>
          <div class="nav-item"><RouterLink :to="{ name:'community'}">커뮤니티</RouterLink></div>
        </div>
        <div class="menu">
          <div class="search">
            <i class="fa-solid fa-magnifying-glass fa-2x" style="color: #ffffff;"></i>
          </div>
          <div v-if="!store.isLogin">
            <RouterLink :to="{ name:'signup'}">회원가입</RouterLink>
            <span> | </span>
            <RouterLink :to="{ name:'login'}">로그인</RouterLink>
          </div>
          <div v-else>
            <a @click="logout" style="padding: 20px;">로그아웃</a>
          </div>
          <RouterLink :to="{ name:'profile'}">프로필</RouterLink>
        </div>
      </header>
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

const logout = function () {
  store.logout()
  router.push({ name: 'login' })
}
</script>

<style scoped>
.header {
  display: flex;
  align-items: center;
  background-color: black;
  padding: 10px 50px;
  position: fixed; /* 네비게이션 바 고정 */
  width: 100%; /* 전체 폭 차지 */
  top: 0; /* 상단에 고정 */
  z-index: 1000; /* 다른 요소들 위에 위치 */
}
a {
  text-decoration-line: none;
  color: #ffffff;
}
.logo {
  height: 50px;
  margin-right: 40px;
}

.nav {
  display: flex;
  flex-grow: 1;
  color: white;
  font-size: 18px;
}

.nav-item {
  padding: 0 20px;
}

.menu {
  display: flex;
  align-items: center;
  color: white;
}

.menu-item {
  padding: 10px;
}

.menu .search {
  padding-right: 30px;
}

.profile {
  margin-left: 20px;
  height: 40px;
  width: 40px;
  border-radius: 10px;
}
.home {
  background-color: black; /* 배경을 검정색으로 설정 */
  padding-top: 80px; /* 네비게이션 바 공간 확보 */
}
</style>
