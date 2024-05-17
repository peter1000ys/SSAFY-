<template>
  <div>
    <h1>회원가입 페이지</h1>
    <form ref="form" @submit.prevent="signup">
      <div>
        <label for="username">username : </label>
        <input type="text" id="username" name="username" />
      </div>

      <div>
        <label for="password1">password : </label>
        <input type="password" id="password1" name="password1" />
      </div>

      <div>
        <label for="password2">password Confirmation : </label>
        <input type="password" id="password2" name="password2" />
      </div>
      <button type="submit">submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";

const form = ref(null)
const router = useRouter()
const store = useUserStore()

const signup = function () {
  const data = new FormData(form.value);
  store.signup(data);
  form.value.reset();
  router.push({ name: "login" });
};
</script>

<style scoped></style>
