<template>
  <div>
    <h3>Comment Create</h3>
    <form @submit.prevent="createComment">
      <div>
        <label for="content">content : </label>
        <!-- <textarea name="content" id="content" cols="30" rows="1" v-model="content"></textarea> -->
        <input type="text" name="content" id="content"  v-model="content">
      </div>
      <button type="submit">create</button>
    </form>
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  import { useCommunityStore } from '@/stores/community';
  import { useUserStore } from '@/stores/user';
  
  const props = defineProps({
    reviewId:String
  })

  const content = ref(null)
  const store = useCommunityStore()
  const userStore = useUserStore()

  const createComment = function() {
    const data = {
      content: content.value,
      user:userStore.userId,
      review:props.reviewId
    }
    store.createComment(data)
    content.value = ""
  }

</script>

<style scoped>

</style>