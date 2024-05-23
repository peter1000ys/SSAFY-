<template >
  <div class="s-container">
    <h1 class="font">리뷰 상세페이지</h1>
    <div class="d-flex align-items-center justify-content-center">
      <div>
        <img
          class="img"
          :src="`https://image.tmdb.org/t/p/w500${review.poster_path}`"
          alt="..."
        />
      </div>
      <div class="ms-4 fs-6">
        <p>영화 제목 : {{ review.movie_title }}</p>
        <p>리뷰 제목 : {{ review.title }}</p>
        <p>리뷰 내용 : {{ review.content }}</p>
        <p>작성자 : {{ review.username }}</p>
        <p>평점 : {{ review.rank }} 점</p>
      <div class="buttons-container">
        <button @click="reviewLike()" class="like-button">
          <span class="badge" v-if="reviewLikeCount > 0">{{ reviewLikeCount }}</span>
          <i class="bi bi-hand-thumbs-up-fill icon-color" v-if="reviewLiked"> </i>
          <i class="bi bi-hand-thumbs-up icon-color" v-else> </i>
          <span class="text-color">{{ reviewLiked ? "좋아요 취소" : "좋아요" }}</span>
        </button>
        <button @click="reviewHate()" class="hate-button">
          <span class="badge" v-if="reviewHateCount > 0">{{ reviewHateCount }}</span>
          <i class="bi bi-hand-thumbs-down-fill icon-color" v-if="reviewHated"> </i>
          <i class="bi bi-hand-thumbs-down icon-color" v-else> </i>
          <span class="text-color">{{ reviewHated ? "싫어요 취소" : "싫어요" }}</span>
        </button>
        <div v-if="review.user === store.userId">
          <button class="btn btn-outline-danger" @click="reviewDelete">리뷰 삭제</button>
        </div>
      </div>
    </div>
  </div>
  <div v-if="review.user === store.userId">
    <hr class="border border-danger border-2 opacity-50">
    <h3 class="text-center">리뷰 수정</h3>
    <RevieUpdate :review="review" />
  </div>
    <div class="">
      <hr class="border border-danger border-2 opacity-50">
      <hr class="border border-danger border-2 opacity-30">
      <h3 class="fs-5 mb-4 font text-center">댓글 목록</h3>
      <hr class="border border-danger border-2 opacity-30">
      
      <CommentList
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"
      />
    </div>

    <div class="">
      <Comment :review-id="reviewId" />
    </div>
  </div>

</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useRouter, useRoute } from "vue-router";
import { useUserStore } from "@/stores/user";
import { useCommunityStore } from "@/stores/community";
import axios from "axios";
import CommentList from "@/components/CommentList.vue";
import Comment from "@/components/Comment.vue";
import RevieUpdate from '@/components/ReviewUpdate.vue'

const store = useUserStore();
const communityStore = useCommunityStore();

const route = useRoute()
const router = useRouter()
const comments = computed(() => communityStore.comments);
const reviewId = ref(route.params.reviewId);
const review = ref({});

const reviewLiked = ref(false);
const reviewHated = ref(false);
const reviewLikeCount = ref(0);
const reviewHateCount = ref(0);

// 리뷰 상세 정보 요청
onMounted(() => {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/api/v1_1/${reviewId.value}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      review.value = response.data;
    })
    .then(() => {
      communityStore.getComments(reviewId.value);
      console.log("코멘트", comments.value);
    });
});

onMounted(() => {
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/api/v1_1/${reviewId.value}/like/${store.userId}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      console.log(response);
      reviewLiked.value = response.data.liked;
      reviewLikeCount.value = response.data.count;
      console.log("리뷰 좋아요 조회 완료");
    })
    .catch((error) => {
      console.log(error);
    });
  axios({
    method: "get",
    url: `http://127.0.0.1:8000/api/v1_1/${reviewId.value}/hate/${store.userId}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      console.log(response);
      reviewHated.value = response.data.hated;
      reviewHateCount.value = response.data.count;
      console.log("리뷰 싫어요 조회 완료");
    })
    .catch((error) => {
      console.log(error);
    });
});

const reviewLike = function () {
  axios({
    method: "post",
    url: `http://127.0.0.1:8000/api/v1_1/${reviewId.value}/like/${store.userId}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      console.log(response);
      reviewLiked.value = response.data.liked;
      reviewLikeCount.value = response.data.count;
      console.log("리뷰 좋아요 완료");
    })
    .catch((error) => {
      console.log(error);
    });
};

const reviewHate = function () {
  axios({
    method: "post",
    url: `http://127.0.0.1:8000/api/v1_1/${reviewId.value}/hate/${store.userId}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      console.log(response);
      reviewHated.value = response.data.hated;
      reviewHateCount.value = response.data.count;
      console.log("리뷰 싫어요 완료");
    })
    .catch((error) => {
      console.log(error);
    });
};

const reviewDelete = function () {
  axios({
    method: "delete",
    url: `http://127.0.0.1:8000/api/v1_1/${reviewId.value}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      console.log(response);
      console.log("리뷰 삭제 완료");
      router.push({name:'community'})
    })
    .catch((error) => {
      console.log(error);
    });
}

// const reviewUpdate = function () {
//   router.push({name:'reviewUpdate', params:{reviewId:reviewId}})
// }

</script>

<style scoped>
.s-container{
  width: 40%;
  margin: 0 auto;
}


.img {
  width: 200px;
}

.icon-color {
  font-size: 30px;
  color: white;
}
.text-color {
  font-size: 20px;
  font-weight: 900;
  color: white;
  
}

.buttons-container {
  display: flex;
  align-items: center;
}

button {
  position: relative;
  padding: 10px;
  border: none;
  background: none;
  cursor: pointer;
  font-size: 16px;
  display: flex;
  align-items: center;
}

.like-button, .hate-button {
  margin-right: 20px;
}

.badge {
  position: absolute;
  top: -10px;
  right: -10px;
  background-color: red;
  color: white;
  border-radius: 30%;
  padding: 5px 10px;
  font-size: 20px;
  display: inline-block;
}

.btn-common {
  /* 공통 스타일을 정의합니다 */
  display: inline-block;
  text-align: center;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: 0.25rem;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}
</style>
