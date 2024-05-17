import axios from "axios";
import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useUserStore = defineStore(
  "user",
  () => {
    const token = ref(null);
    const isLogin = computed(() => {
      if (token.value === null) {
        return false;
      } else {
        return true;
      }
    });
    // 회원가입
    const signup = function (data) {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data,
      }).then((response) => {
        console.log(response);
      });
    };

    // 로그인
    const login = function (data) {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/login/",
        data,
      }).then((response) => {
        console.log(response);
        token.value = response.data.key;
        console.log(token.value);
      });
    };

    // 로그아웃
    const logout = function () {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/logout/",
      }).then((response) => {
        console.log(response);
        console.log("로그아웃되었습니다.");
        token.value = null
        console.log(token.value);
      });
    };

    return { token, signup, login, logout, isLogin };
  },
  { persist: true }
);
