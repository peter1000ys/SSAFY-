import axios from "axios";
import { ref, computed } from "vue";
import { defineStore } from "pinia";
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

export const useCommunityStore = defineStore("community",() => {
    const router = useRouter()
    const reviews = ref([])
    const comments = ref([])
    const store = useUserStore()
    
    const reviewLiked = ref(false)
    const reviewHated = ref(false)
    const reviewLikeCount = ref(0)
    const reviewHateCount = ref(0)

    // 리뷰 조회
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
        getReviews()
      })
        .catch((error) => {
          console.log(error)
        })
      router.push({name:"home"})
    };

    const getComments = function (review) {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1_1/${review}/comment/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      }).then((response) => {
        console.log(response);
        comments.value = response.data
      });
    };

    const createComment = function (data) {
      const { content, user, review } = data
      console.log(content)
      console.log(user)
      console.log(review)
      axios({
        method: "post",
        url:`http://127.0.0.1:8000/api/v1_1/${review}/comment/`,
        data: {
          content, user, review
        },
        headers: {
          Authorization: `Token ${store.token}`
        }
      }).then((response) => {
        console.log(response)
        console.log("코멘트 작성 완료")
        router.push({name:"community"})
      })
        .catch((error) => {
          console.log(error)
        })
    }

    const reviewLike = function (data) {
      const { user, review } = data
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/api/v1_1/${review}/like/${user}/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      }).then((response) => {
        console.log(response)
        reviewLiked.value = response.data.liked
        reviewLikeCount.value = response.data.count
        console.log("리뷰 추천 완료")
      })
        .catch((error) => {
          console.log(error)
      })
    }

    const reviewHate = function (data) {
      const { user, review } = data
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/api/v1_1/${review}/hate/${user}/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      }).then((response) => {
        console.log(response)
        reviewHated.value = response.data.hated
        reviewHateCount.value = response.data.count
        console.log("리뷰 싫어요 완료")
      })
        .catch((error) => {
          console.log(error)
      })
    }

    return { reviews, comments, getReviews, createReview, getComments, createComment, reviewLiked, reviewHated, reviewLikeCount, reviewHateCount, reviewLike, reviewHate };
  },
  { persist: true }
);
