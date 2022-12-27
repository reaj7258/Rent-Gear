import { createRouter, createWebHistory } from 'vue-router'

import Home from '../views/HomeAdmin.vue'
import Login from '../views/login.vue'


function guardMyroute(to, from, next){
  var isAuthenticated= false; 
  if(localStorage.getItem('email') != null){
    isAuthenticated = true;
  }
  else{
    isAuthenticated= false;
  }
    
  if(isAuthenticated) 
  {
    next();
  } 
  else
  {
    next('/');
  }
}

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login,
    // beforeEnter : guardMyroute,
    
  },
  {
    path: '/register',
    name: 'register',
    component: () => import(/* webpackChunkName: "about" */ '../views/register.vue'),
    // beforeEnter : guardMyroute,
  },
  {
    path: '/home',
    name: 'Home',
    component: Home,
    beforeEnter : guardMyroute,
  },
  {
    path: '/home_cus',
    name: 'My Adds',
    component: () => import(/* webpackChunkName: "about" */ '../views/HomeCustomer.vue'),
    beforeEnter : guardMyroute,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import(/* webpackChunkName: "about" */ '../views/Dashboard.vue'),
    beforeEnter : guardMyroute,
  },
  {
    path: '/product_details/:name',
    name: 'ProductDetails',
    component: () => import(/* webpackChunkName: "about" */ '../views/ProductDetails.vue'),
    beforeEnter : guardMyroute,
  },
  {
    path: '/product_details2/:id',
    name: 'ProductDetails2',
    component: () => import(/* webpackChunkName: "about" */ '../views/ProductDetails2.vue'),
    beforeEnter : guardMyroute,
  },
  {
    path: '/product_add',
    name: 'Create Add',
    component: () => import(/* webpackChunkName: "about" */ '../views/ProductAdd.vue'),
    beforeEnter : guardMyroute,
  },
  {
    path: '/category_add',
    name: 'Category Add',
    component: () => import(/* webpackChunkName: "about" */ '../views/CategoryAdd.vue'),
    beforeEnter : guardMyroute,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
