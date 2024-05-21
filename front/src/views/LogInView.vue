<template>
  <div>
    <h1>로그인 페이지</h1>
    <form ref="form" @submit.prevent="login">
      <div>
        <label for="username">username : </label>
        <input type="text" name="username" id="username" v-model="username">
      </div>

      <div>
        <label for="password">password : </label>
        <input type="password" name="password" id="password">
      </div>

      <button type="submit">submit</button>

    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from "vue-router";
import { useUserStore } from '@/stores/user'

const form = ref(null)
const router = useRouter()
const store = useUserStore()
const username = ref("")

const login = function () {
  const data = new FormData(form.value)
  store.login(data, username)
  form.value.reset()
  router.push({ name: "home" })
} 
</script>

<style scoped>
</style>
