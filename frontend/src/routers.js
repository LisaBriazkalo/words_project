import {createRouter, createWebHistory} from 'vue-router'
import Home from './components/Home.vue'
import Dictionary from './components/Dictionary.vue'
import WordDetails from './components/WordDetails.vue'
import CreateWord from './components/CreateWord.vue'
import WordEdit from './components/WordEdit.vue'

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
    },
    {
        path: '/:categoryName/:id/wordEdit',
        name: 'wordEdit',
        component: WordEdit,
        props: true
    },
    {
        path: '/:categoryName/create',
        name: 'CreateWord',
        component: CreateWord,
        props: true
    }
]

const router=createRouter({
    history: createWebHistory(),
    routes
})

export default router;