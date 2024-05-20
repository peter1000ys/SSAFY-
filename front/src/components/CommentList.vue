<template>
  <div>
    <p>
      {{ comment.id }}번 | {{ comment.content }} | {{ comment.user }}번 유저 |
      {{ comment.review }}번 리뷰
    </p>
    <button @click="commentLike()">
      {{ commentLiked ? "좋아요 취소" : "좋아요" }}
    </button>
    <button @click="commentHate()">
      {{ commentHated ? "싫어요 취소" : "싫어요" }}
    </button>
    <p>좋아요 수 : {{ commentLikeCount }}</p>
    <p>싫어요 수 : {{ commentHateCount }}</p>
    <hr>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import axios from "axios";

const props = defineProps({
  comment: Object,
});
console.log(
  "코멘트 정보",
  props.comment.id,
  props.comment.review,
  props.comment.user
);
const commentLiked = ref(false);
const commentHated = ref(false);
const commentLikeCount = ref(0);
const commentHateCount = ref(0);

const store = useUserStore();

const commentLike = function () {
  axios({
    method: "post",
    url: `http://127.0.0.1:8000/api/v1_1/${props.comment.review}/comment/${props.comment.id}/like/${props.comment.user}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      console.log(response)
      commentLiked.value = response.data.liked
      commentLikeCount.value = response.data.count
      console.log("코멘트 좋아요 완료")
    })
    .catch((error) => {
      console.log(error)
    });
};

const commentHate = function () {
  axios({
    method: "post",
    url: `http://127.0.0.1:8000/api/v1_1/${props.comment.review}/comment/${props.comment.id}/hate/${props.comment.user}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      console.log(response)
      commentHated.value = response.data.hated
      commentHateCount.value = response.data.count
      console.log("코멘트 싫어요 완료");
    })
    .catch((error) => {
      console.log(error)
    });
};

onMounted(() => {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/api/v1_1/${props.comment.review}/comment/${props.comment.id}/like/${props.comment.user}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      console.log(response)
      commentLiked.value = response.data.liked
      commentLikeCount.value = response.data.count
      console.log("코멘트 좋아요 조회 완료")
    })
    .catch((error) => {
      console.log(error)
    })
    
    axios({
    method: "get",
    url: `http://127.0.0.1:8000/api/v1_1/${props.comment.review}/comment/${props.comment.id}/hate/${props.comment.user}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      console.log(response)
      commentHated.value = response.data.hated
      commentHateCount.value = response.data.count
      console.log("코멘트 싫어요 조회 완료");
    })
    .catch((error) => {
      console.log(error)
    })
})

</script>

<style scoped></style>
