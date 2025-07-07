import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import('@/views/homeView.vue')
        },
        {
            path: '/analysis',
            name: 'analysis',
            component: () => import('@/views/analysisView.vue')
        },
        {
            path: '/settings',
            name: 'settings',
            component: () => import('@/views/settingsVies.vue')
        }
    ]
})

export default router