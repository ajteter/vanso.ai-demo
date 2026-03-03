import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: '/',
        name: 'Landing',
        component: () => import('../views/LandingPage.vue'),
    },
    {
        path: '/studio',
        component: () => import('../views/StudioLayout.vue'),
        children: [
            {
                path: '',
                name: 'Dashboard',
                component: () => import('../views/DashboardPage.vue'),
            },
            {
                path: 'new-drop',
                name: 'NewDrop',
                component: () => import('../views/NewDropPage.vue'),
            },
            {
                path: 'my-drops',
                name: 'MyDrops',
                component: () => import('../views/MyDropsPage.vue'),
            },
        ],
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
