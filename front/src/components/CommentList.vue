
<!-- 안쓰는 페이지 삭제 예정 -->
<!--  -->
<!--  -->

<template>
  <div>
    <h3>Comment List</h3>
    <!-- <div v-for="comment in comments" :key="comment.id"> -->
    <div>{{comment.id}}번 | {{ comment.content }} | {{ comment.user }}번 유저 | {{ comment.review}} 번 리뷰 </div>
    <!-- </div> -->
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { useCommunityStore } from '@/stores/community';
  import { useUserStore } from '@/stores/user';
  
  const props = defineProps({
    reviewId:String,
    comment:Array
  })
  console.log("리뷰id", props.reviewId)

  const store = useCommunityStore()
  const userStore = useUserStore()

  // onMounted(() => {
  //   store.getComments(props.reviewId)
  // })
  // const comments = store.comments
</script>

<style scoped>

</style>