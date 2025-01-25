import { createRouter, createWebHistory } from 'vue-router'

import readDataView from '@/views/readDataView.vue'
import serverControlView from '@/views/serverControlView.vue'
import userSignView from '@/views/userSignView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'read-data',
      component: readDataView,
      props: true
    },
    {
      path: '/user/write',
      name: 'ctrl-panel',
      component: serverControlView,
      props: true
    },
    {
      path: '/user/authorise',
      name: 'sign-in',
      component: userSignView,
    },
  ]
})

export default router
