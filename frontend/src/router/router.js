import Vue from 'vue';
import Router from 'vue-router';
import Home from 'src/components/Home/Home';
import CollectTaskContainer from 'src/components/CollectTaskContainer/CollectTaskContainer';
import CollectTask from 'src/components/CollectTask/CollectTask';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [{
    path: '/',
    name: 'Главная',
    component: Home
  }, {
    path: '/collect-tasks',
    component: CollectTaskContainer,
    children: [{
      path: ':id',
      component: CollectTask,
      props: {}
    }]
  },]
});
