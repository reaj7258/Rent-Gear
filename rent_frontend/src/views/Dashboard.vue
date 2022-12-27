<template>
  <div style="height: full">
    <div class="grid grid-cols-8">
      <div class="col-span-1"></div>
      <div class="col-span-6 mt-20">
        <div class="grid grid-cols-3">
          <div @click="Select(d.name)" class="col-span-1 m-2 p-10 rounded-lg hover:bg-blue-700 hover:text-white cursor-pointer bg-blue-100 text-2xl" v-for="d in data" :key="d">{{ d.name }}</div>
        </div>
      </div>
      <div class="col-span-1"></div>
    </div>
  </div>
</template>

<script>
import api from '../../boot/axios';
import { notify } from 'notiwind';

export default {
  name: 'login',
  data() {
    return {
      data: [],
    };
  },
  created() {
    this.getData();
  },
  methods: {
    Select(name) {
      this.$router.push({ name: 'ProductDetails', params: { name: name } });
    },
    async getData() {
      await api
        .get(`api/category/`)
        .then((response) => {
          this.data = response.data;
          console.table(this.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>