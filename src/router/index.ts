import {createRouter, createWebHistory} from 'vue-router';
import Home from "../components/home/Home.vue";
import Question from "@/components/Questions/Question.vue";

const routes = [
    {
        path: '/',
        redirect: '/home',
    },
    {
        path: '/home',
        name: 'Home',
        component: Home
    },
    {
        path: '/authentication/:type',
        name: 'auth',
        component: () => import("@/components/authentication/index.vue")
    },
    {
        path: '/Question',
        name: 'Questions',
        component: Question
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;