import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/Home.vue";
import Login from "../components/Login.vue";
import Registration from "../components/Registration.vue";
import Main from "../components/Main.vue";
import Products from "../components/Products.vue";

export default createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: Home },
    { path: "/login", component: Login },
    { path: "/registration", component: Registration },
    {
      path: "/main",
      component: Main,
      props: true,  
      children: [
        {
          path: "games",
          component: Products,
        },
      ],
    },
  ],
});
