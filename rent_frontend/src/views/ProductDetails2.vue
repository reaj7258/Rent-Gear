<template>
  <div style="height: full">
    <div class="grid grid-cols-5">
      <div class="col-span-1"></div>
      <div class="col-span-1 mt-20"><img :src="dataPic.pic" alt="" class="w-full p-1 rounded-lg" /></div>
      <div class="col-span-1 mt-20"><img :src="dataPic.pic2" alt="" class="w-full p-1 rounded-lg" /></div>
      <div class="col-span-1 mt-20"><img :src="dataPic.pic3" alt="" class="w-full p-1 rounded-lg" /></div>
      <div class="col-span-1"></div>
      <div class="col-span-1"></div>
      <div class="col-span-3 mt-5 text-left p-5 rounded-xl bg-blue-100">
        <p class="text-4xl py-5">
          <span class="font-bold">Title: </span><span class="italic">{{ data.title }}</span>
        </p>
        <p class="text-3xl pb-5">
          <span class="font-bold">Rent Amount per Day: </span><span>{{ data.amount }}</span>
        </p>
        <p class="text-3xl pb-5">
          <span class="font-bold">Contact: </span><span>{{ data.phone }}</span>
        </p>
        <p class="text-3xl pb-5">
          <span class="font-bold">Description: </span><span class="italic">{{ data.description }}</span>
        </p>
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
      dataPic: [],
      id: this.$route.params.id,
    };
  },
  created() {
    this.getData();
  },
  methods: {
    async getData() {
      await api
        .get(`api/add_pic/?add=${this.id}`)
        .then((response) => {
          this.dataPic = response.data[0];
          console.table(this.dataPic);
        })
        .catch((error) => {
          console.log(error);
        });
      await api
        .get(`api/add/${this.id}/`)
        .then((response) => {
          this.data = response.data;
          //   console.table(this.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>