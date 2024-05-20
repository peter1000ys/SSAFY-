<template>
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">공식 예고편</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="closeModal"></button>
          </div>
          <div class="modal-body" v-if="store.movieVideoKey">
            <iframe id="player" type="text/html" width="400" height="300"
              :src="`http://www.youtube.com/embed/${store.movieVideoKey}`"
              frameborder="0"></iframe>
          </div>
          <div v-else>
            <p>트레일러 존재하지 않음</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import { useMovieStore } from '@/stores/movie'
  
  const store = useMovieStore()
  const router = useRouter()
  const route = useRoute()
  const movieId = route.params.movieId
  
  const closeModal = () => {
    const iframe = document.getElementById('player')
    if (iframe) {
      iframe.src = ''
    }
    router.push({ name: 'detail', params: { movieId: movieId } })
  }
  
  onMounted(() => {
    const modalElement = document.getElementById('exampleModal')
    modalElement.addEventListener('hidden.bs.modal', () => {
      const iframe = document.getElementById('player')
      if (iframe) {
        iframe.src = ''
      }

    })
  })
  </script>
  
  <style scoped>
  .should-show {
    display: block;
  }
  </style>
  