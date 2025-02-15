import './assets/main.scss'
import router from './router'
import App from './App.vue'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

const app = createApp(App)
app.use(createPinia())
app.use(router)

app.mount('#app')