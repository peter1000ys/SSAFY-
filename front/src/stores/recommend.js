import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useRecommendStore = defineStore('recommend', () => {
  const weekday = ref([])

  const getTodayRecommend = function() {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/movies/recommend/weekday/'
    })
    .then((res) => {
      console.log(res)
      weekday.value = res.data
    })
  }
  return {weekday, getTodayRecommend}
}, { persist: true })
