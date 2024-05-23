import { createRouter, createWebHistory, useRoute } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import MovieListView from '@/views/MovieListView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import CommunityView from '@/views/CommunityView.vue'
import ReviewDetailView from '@/views/ReviewDetailView.vue'
import ProfileView from '@/views/ProfileView.vue'
import SearchView from '@/views/SearchView.vue'
import SearchModalView from '@/views/SearchView.vue'
import RelatedMovie from '@/components/RelatedMovie.vue'
import ReviewList from '@/components/ReviewList.vue'
import Genre from '@/components/Genre.vue'

import ReviewCreate from '@/components/ReviewCreate.vue'
import ReviewUpdate from '@/components/ReviewUpdate.vue'

import Comment from '@/components/Comment.vue'

import { useCommunityStore } from '@/stores/community'
import { useMovieStore } from '@/stores/movie'
import { useRecommendStore } from '@/stores/recommend'
// 라우터 네임 확인하고 사용하기!!
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      // beforeEnter:(to, from) => {
      //   const store = useMovieStore()
      //   const recommendStore = useRecommendStore()
      //   store.myFavoriteMovie()
      //   recommendStore.userRecommend()
      //   console.log("실행됨")

      // }
    },
    {
      path: '/movies/',
      name: 'list',
      component: MovieListView,
      children:[
        {
          path: 'genre/:genreId',
          name: 'genre',
          component: Genre,
        },
      ]
    },
    {
      path: '/:movieId',
      name: 'detail',
      component: MovieDetailView,
      children: [
        {path:'related', name:'related', component:RelatedMovie,},
        {path:'review', name:'review', component:ReviewList},
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: LogInView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView,
      children:[
        {path:'create', name:'create', component:ReviewCreate},
      ]
    },
    {
      path: '/community/:reviewId',
      name: 'reviewDetail',
      component: ReviewDetailView,
      children:[
        {path:'comment', name:'comment', component:Comment},
      ]
    },
    {
      path:'/update/:reviewId',
      name:'reviewUpdate',
      component:ReviewUpdate,
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    }
    ,
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
  ]
})


export default router
