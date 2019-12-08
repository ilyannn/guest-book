import 'bootstrap/dist/css/bootstrap.css';
import Vue from 'vue';
import { BAlert } from 'bootstrap-vue';
import App from './App.vue';
import router from './router';

Vue.component('b-alert', BAlert);
Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
