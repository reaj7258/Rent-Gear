<template>
  <div>
    <div v-if="currentRouteName != 'login' && currentRouteName != 'register'">
      <NavbarCustomer />
      <router-view />
    </div>
    <div v-else>
      <router-view />
    </div>
  </div>
</template>
<script>
import './assets/tailwind.css';

import NavbarCustomer from '@/components/NavbarCustomer';

export default {
  components: { NavbarCustomer },
  data() {
    return {};
  },
  computed: {
    currentRouteName() {
      // console.log(this.$route.name);
      return this.$route.name;
    },
  },

  methods: {},
};
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>