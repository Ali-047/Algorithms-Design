import {createRouter, createWebHistory} from 'vue-router';
import Home from "../components/home/Home.vue";

const routes = [
    {
        path: '/',
        redirect: '/home',
    },
    {
        path: '/home',
        name: 'Home',
        component:Home
    },
    {
        path: '/authentication/:type',
        name:'auth',
        component:() =>import("@/components/authentication/index.vue")
    },
    {
        path: '/home/questions',
        name: 'Questions',
        component:() => import("@/components/Questions/Question.vue")
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;