<template>
  <div style="height: full">
    <div class="grid grid-cols-6">
      <div class="col-span-1"></div>
      <div v-if="data.length == 0" class="col-span-4 mt-20">
        <p class="text-5xl font-bold">No Add in this Category</p>
      </div>
      <div v-else class="col-span-4 mt-10">
        <div class="grid grid-cols-2">
          <div v-for="d in data" :key="d" @click="Select(d.id)" class="col-span-2 box bg-blue-100 hover:bg-blue-200 rounded-lg shadow-lg p-5 m-5 cursor-pointer">
            <div class="grid grid-cols-4">
              <div class="col-span-1 m-1">
                <img :src="d.pic" class="h-40 w-40" />
              </div>
              <div class="col-span-3 py-2 ml-10">
                <p class="text-3xl p-1 mb-1 text-left">Title: {{ d.title }}</p>
                <p class="text-2xl p-1 text-left">Amount: {{ d.amount }}</p>
                <p class="text-2xl p-1 text-left">Description: {{ d.description }}</p>
              </div>
            </div>
          </div>
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
      dataPic: [],
      name: this.$route.params.name,
    };
  },
  created() {
    this.getData();
  },
  methods: {
    Select(a) {
      this.$router.push({ name: 'ProductDetails2', params: { id: a } });
    },
    async getData() {
      console.log(this.name);
      let a = this.name.split(' ');
      let b = '';
      if (a.length != 1) {
        for (let i = 0; i < a.length; i++) {
          b += a[i] + '+';
        }
        b = b.slice(0, -1);
      } else {
        b = this.name;
      }
      console.log(b);
      await api
        .get(`api/add_pic/`)
        .then((response) => {
          this.dataPic = response.data;
          //   console.table(this.dataPic);
        })
        .catch((error) => {
          console.log(error);
        });
      await api
        .get(`api/add/?category=${b}`)
        .then((response) => {
          this.data = response.data;
          //   console.table(this.data);
        })
        .catch((error) => {
          console.log(error);
        });
      for (let i = 0; i < this.data.length; i++) {
        for (let j = 0; j < this.dataPic.length; j++) {
          if (this.data[i].id == this.dataPic[j].add) {
            this.data[i].pic = this.dataPic[j].pic;
            this.data[i].pic2 = this.dataPic[j].pic2;
            this.data[i].pic3 = this.dataPic[j].pic3;
          }
        }
      }
      console.table(this.data);
    },
  },
};
</script>