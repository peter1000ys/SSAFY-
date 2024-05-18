<template>
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">공식 예고편</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <iframe id="player" type="text/html" width="400" height="300"
                    :src="`http://www.youtube.com/embed/${store.movieVideoKey}/`"
                    frameborder="0"></iframe>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()
</script>

<style scoped>
.should-show {
    display: block;
}
</style>