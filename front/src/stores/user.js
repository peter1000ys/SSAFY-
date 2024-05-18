import axios from "axios";
import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useUserStore = defineStore("user", () => {
    const token = ref(null)
    const loginUsername = ref(null)
    const userId = ref(null)

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
    const login = function (data, username) {
      // console.log(username.value)
      
      // console.log(loginUsername.value)
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/login/",
        data,
      }).then((response) => {
        loginUsername.value = username.value
        token.value = response.data.key;
        console.log(token.value);
        console.log(token);
        console.log(loginUsername.value)

        axios({
          method: "get",
          url: `http://127.0.0.1:8000/api/v1_2/${loginUsername.value}/`,
          headers: {
            Authorization: `Token ${token.value}`
          }
          })
          .then((response) => {
            // console.log(response);
            userId.value = response.data.id
            console.log(userId.value)
          })

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

    return { token, signup, login, logout, isLogin, loginUsername, userId };
  },
  { persist: true }
);
