import { createWebHistory, createRouter } from 'vue-router'
import HelloWorld from '../components/HelloWorld.vue'
import Sequence from '../components/Sequence.vue'
import animation from '../components/animation.vue'
import Material from '../components/Material.vue'
import Lighting from '../components/Lighting.vue'
import Utl from '../components/Utl.vue'
import Check from '../components/Check.vue'
import Scripts from '../components/Scripts.vue'
const routes = [
  { path: '/test', component: HelloWorld, meta: { keepAlive: true }},
  { path: '/sequence', component: Sequence , meta: { keepAlive: true }},
  { path: '/animation', component: animation , meta: { keepAlive: true }},
  { path: '/material', component: Material , meta: { keepAlive: true }},
  { path: '/lighting', component: Lighting , meta: { keepAlive: true }},
  { path: '/utl', component: Utl , meta: { keepAlive: true }},
  { path: '/check', component: Check , meta: { keepAlive: true }},
  { path: '/scripts', component: Scripts , meta: { keepAlive: true }},
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router