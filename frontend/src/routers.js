import {createRouter, createWebHistory} from 'vue-router'
import Home from './components/Home.vue'
import Dictionary from './components/Dictionary.vue'
import WordDetails from './components/WordDetails.vue'

const routes=[
    {
        path: '/',
        name: 'home',
        component: Home
    },

    {
        path: '/:name/dictionary',
        name: 'dictionary',
        component: Dictionary,
        props: true
    },
    {
        path: '/:categoryName/:id/wordDetails',
        name: 'wordDetails',
        component: WordDetails,
        props: true
    }
]

const router=createRouter({
    history: createWebHistory(),
    routes
})

export default router;