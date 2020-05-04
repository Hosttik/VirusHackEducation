import Vue from 'vue';
import Router from 'vue-router';
import Home from 'src/components/Home/Home';
import CollectTaskContainer from 'src/components/CollectTaskContainer/CollectTaskContainer';
import CollectTask from 'src/components/CollectTask/CollectTask';
import Collection from 'src/components/Collection/Collection';
import ShareCollection from 'src/components/ShareCollection/ShareCollection';
import Lk from 'src/components/Lk/Lk';

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
  }, {
    path: '/collection',
    name: 'Коллекция',
    component:Collection
  }, {
    path:'/share-collection',
    name:'Задание',
    component:ShareCollection
  }, {
    path:'/lk',
    name:'Личный кабинет',
    component:Lk
  }]
});
