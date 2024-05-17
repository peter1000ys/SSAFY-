import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useMovieStore = defineStore('movie', () => {
  const genres = ref([])
  const movies = ref([])
  const filteredMovies = ref([])
  const getGenres = function() {
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/api/v1/movies/genres'
    })
    .then((res) => {
      console.log(res)
      genres.value = res.data
    })

  }
  const getMovies = function() {
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/api/v1/movies/'
    })
    .then((res) => {
      console.log(res)
      movies.value = res.data
    })
  }
  const filterMovie = function(genreId) {
    filteredMovies.value = null
    axios({
      method:'get',
      url:`http://127.0.0.1:8000/api/v1/filter-genre/${genreId}/`
    })
    .then((res) => {
      console.log(res)
      filteredMovies.value = res.data
    })
  }

  return { genres, getGenres, movies, getMovies, filterMovie, filteredMovies }
}, { persist: true})
