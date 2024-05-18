import axios from "axios";
import { ref, computed } from "vue";
import { defineStore } from "pinia";
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

export const useCommunityStore = defineStore("community",() => {
    const router = useRouter()
    const reviews = ref([]);
    const store = useUserStore()

    // 회원가입
    const getReviews = function () {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/api/v1_1/reviews/",
        headers: {
          Authorization: `Token ${store.token}`
        }
      }).then((response) => {
        console.log(response);
        reviews.value = response.data
      });
    };

    const createReview = function (data) {
      const { title, movie_title, content, rank, user } = data
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/v1_1/reviews/",
        data: {
          title,
          movie_title,
          rank,
          content,
          user
        },
        headers: {
          Authorization: `Token ${store.token}`
        }
      }).then((response) => {
        console.log(response)
        console.log("작성 완료")
      })
        .catch((error) => {
          console.log(error)
        })
      router.push({name:"community"})
    };

    return { reviews, getReviews, createReview };
  },
  { persist: true }
);
