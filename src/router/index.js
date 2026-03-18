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
                path: 'statistics',
                name: 'Statistics',
                component: () => import('../views/StatisticsPage.vue'),
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
    {
        path: '/v1',
        name: 'LandingV1',
        component: () => import('../v1_views/LandingPage.vue'),
    },
    {
        path: '/v1/studio',
        component: () => import('../v1_views/StudioLayout.vue'),
        children: [
            {
                path: '',
                name: 'DashboardV1',
                component: () => import('../v1_views/DashboardPage.vue'),
            },
            {
                path: 'new-drop',
                name: 'NewDropV1',
                component: () => import('../v1_views/NewDropPage.vue'),
            },
            {
                path: 'my-drops',
                name: 'MyDropsV1',
                component: () => import('../v1_views/MyDropsPage.vue'),
            },
        ],
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
