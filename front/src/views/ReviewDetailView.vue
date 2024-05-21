
<template>
  <div>
    <h1>ReviewDetailView</h1>
    <div>
      <img class="img" :src="`https://image.tmdb.org/t/p/w500${review.poster_path}`" alt="...">
      <p>번호 : {{ review.id }}</p>
      <p>영화 제목 : {{ review.movie_title }}</p>
      <p>리뷰 제목 : {{ review.title }}</p>
      <p>리뷰 내용 : {{ review.content }}</p>
      <p>작성자 : {{ review.user }}</p>
      <p>평점 : {{ review.rank }} 점</p>
        <button @click="reviewLike()">{{reviewLiked? '좋아요 취소':'좋아요'}}</button>
        <button @click="reviewHate()">{{reviewHated? '싫어요 취소':'싫어요'}}</button>
        <p>좋아요 수 : {{reviewLikeCount}}</p>
        <p>싫어요 수 : {{reviewHateCount}}</p>
      <hr>
    </div>
    <h3>Comment List</h3>
    <CommentList v-for="comment in comments" :key="comment.id" :comment="comment"/>
    <div>
      <Comment :review-id="reviewId"/>
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted, computed } from 'vue'
  import { useRoute } from 'vue-router'
  import { useUserStore } from '@/stores/user'
  import { useCommunityStore } from '@/stores/community'
  import axios from 'axios'
  import CommentList from '@/components/CommentList.vue'
  import Comment from '@/components/Comment.vue'

  const store = useUserStore()
  const communityStore = useCommunityStore()

  const route = useRoute()
  const comments = computed(() => communityStore.comments)
  const reviewId = ref(route.params.reviewId)
  const review = ref({})
  console.log("리뷰id", reviewId.value)

  const reviewLiked = ref(false)
  const reviewHated = ref(false)
  const reviewLikeCount = ref(0)
  const reviewHateCount = ref(0)

  // 리뷰 상세 정보 요청
  onMounted(() => {
    axios({
      method: "get",
      url: `http://127.0.0.1:8000/api/v1_1/${reviewId.value}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    }).then((response) => {
      // console.log(response);
      review.value = response.data
      // console.log(review.value)
    }).then(() => {
      communityStore.getComments(reviewId.value)
      // comments.value = communityStore.comments
      console.log("코멘트", comments.value)
    })
  })

  onMounted(() => {
    axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1_1/${reviewId.value}/like/${store.userId}/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      }).then((response) => {
        console.log(response)
        reviewLiked.value = response.data.liked
        reviewLikeCount.value = response.data.count
        console.log("리뷰 좋아요 조회 완료")
      })
        .catch((error) => {
          console.log(error)
      })
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1_1/${reviewId.value}/hate/${store.userId}/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      }).then((response) => {
        console.log(response)
        reviewHated.value = response.data.hated
        reviewHateCount.value = response.data.count
        console.log("리뷰 싫어요 조회 완료")
      })
        .catch((error) => {
          console.log(error)
      })
  })
  
  const reviewLike = function () {
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/api/v1_1/${reviewId.value}/like/${store.userId}/`,
        headers: {
          Authorization: `Token ${store.token}`
        }
      }).then((response) => {
        console.log(response)
        reviewLiked.value = response.data.liked
        reviewLikeCount.value = response.data.count
        console.log("리뷰 좋아요 완료")
      })
        .catch((error) => {
          console.log(error)
      })
    }

    const reviewHate = function () {
      axios({
        method: "post",
        url: `http://127.0.0.1:8000/api/v1_1/${reviewId.value}/hate/${store.userId}/`,
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

</script>

<style scoped>
  .img{
    width: 100px;
  }
</style>