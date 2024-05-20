import axios from "axios";
import { ref, computed } from "vue";
import { defineStore } from "pinia";
import { useRecommendStore } from "./recommend";

export const useUserStore = defineStore("user", () => {
    const token = ref(null)
    const loginUsername = ref(null)
    const userId = ref(null)
    const user = ref({})

    const isLogin = computed(() => {
      return token.value !== null;
    });

    const signup = function (data) {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data,
      }).then((response) => {
        console.log(response);
      });
    };

    const login = function (data, username) {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/login/",
        data,
      }).then((response) => {
        loginUsername.value = username.value
        token.value = response.data.key
        console.log(token.value)
        console.log(loginUsername.value)
        
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
          
          const RecStore = useRecommendStore()
          RecStore.getLikedGenresWithMovies(userId.value)
        })
      })
    }

    const logout = function () {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/logout/",
      }).then((response) => {
        console.log(response);
        console.log("로그아웃되었습니다.");
        token.value = null
        userId.value = null

        const RecStore = useRecommendStore()
        RecStore.clearLikedGenres()
      });
    };

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
