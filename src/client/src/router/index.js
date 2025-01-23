import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: ChannelListView,
    },
    {
      path: '/model/:id',
      name: 'edit-channel',
      component: () => import('@/views/ChannelEditView.vue'),
      props: true
    }
  ]
})

export default router
