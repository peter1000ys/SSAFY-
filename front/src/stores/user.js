import axios from "axios";
import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useUserStore = defineStore("user", () => {
    const token = ref(null)
    // 로그인 된 유저의 유저네임 변수
    const loginUsername = ref(null)
    // 로그인 된 유저 id 변수
    const userId = ref(null)
    const user = ref({})

    // 로그인(토큰) 여부 확인 변수
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
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/login/",
        data,

      // 로그인 및 로그인한 유저 네임 저장
      }).then((response) => {
        loginUsername.value = username.value
        token.value = response.data.key
        console.log(token.value)
        console.log(token)
        console.log(loginUsername.value)
        
        // 저장된 유저네임으로 유저 id 저장
        axios({
          method: "get",
          url: `http://127.0.0.1:8000/api/v1_2/${loginUsername.value}/`,
          headers: {
            Authorization: `Token ${token.value}`
          }
          })
          .then((response) => {
            userId.value = response.data.id
            console.log(userId.value)
          })
      })
    }

    // 로그아웃
    const logout = function () {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/logout/",
      }).then((response) => {
        console.log(response);
        console.log("로그아웃되었습니다.");
        token.value = null
        userPk.value = null
        console.log(token.value);
      });
    };

    // 프로필용 유정 정보 저장
    const profile = function () {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1_2/${userId.value}/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
        })
        .then((response) => {
          console.log(response)
          user.value = response.data
        })
    }

    return { token, signup, login, logout, isLogin, loginUsername, userId, user, profile };
  },
  { persist: true }
);
