import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import MovieListView from '@/views/MovieListView.vue'

import RelatedMovie from '@/components/RelatedMovie.vue'
import ReviewList from '@/components/ReviewList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/movies',
      name: 'list',
      component: MovieListView
    },
    {
      path: '/:movieId',
      name: 'detail',
      component: MovieDetailView,
      children: [
        {path:'related', name:'related', component:RelatedMovie},
        {path:'review', name:'review', component:ReviewList},
      ]
    },

  ]
})

export default router
