import Vue from 'vue';
import VueRouter from 'vue-router';
import Messages from '../components/Messages.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Messages',
    component: Messages,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
