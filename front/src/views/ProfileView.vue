<template>
  <div>
    <h1>Profile</h1>
    <img src="@/assets/profile.jpg" alt="#">
    <!-- {{ store.user }} -->
    <div>
      <h3> 닉네임 : {{ user.username}}</h3>
    </div>
    <hr>
    <div>
      <h3>찜한 영화 목록</h3>
    </div>
  </div>
</template>

<script setup>
  import { onMounted, ref, computed } from 'vue'
  import { useUserStore } from '@/stores/user'

  const store = useUserStore()
  const user = ref({})

  onMounted(() => {
    store.profile()
    user.value = store.user
  })
</script>

<style scoped>

</style>