<template>
  <div style="height: full">
    <div class="grid grid-cols-6">
      <div class="col-span-1"></div>
      <div v-if="data.length == 0" class="col-span-4 mt-20"></div>
      <div v-else class="col-span-4 mt-10">
        <div class="grid grid-cols-2">
          <div v-for="d in data" :key="d" class="col-span-2 box bg-blue-100 rounded-lg shadow-lg p-5 m-5">
            <div class="grid grid-cols-4">
              <div class="col-span-2 py-2 ml-10">
                <p class="text-3xl p-2 text-left">Title : {{ d.title }}</p>
                <p class="text-3xl p-2 text-left">Amount : {{ d.amount }}</p>
                <p class="text-3xl p-2 text-left">Category : {{ d.category }}</p>
              </div>
              <div class="col-span-2 py-2">
                <p class="text-3xl p-2 text-left">Description : {{ d.description }}</p>
                <p class="text-3xl p-2 text-left">Phone : {{ d.phone }}</p>
              </div>
              <div class="col-span-1 m-2">
                <img :src="d.pic" class="h-40 w-40" />
              </div>
              <div v-if="d.pic2 != null" class="col-span-1 m-2">
                <img :src="d.pic2" class="h-40 w-40" />
              </div>
              <div v-if="d.pic2 != null" class="col-span-1 m-2">
                <img :src="d.pic3" class="h-40 w-40" />
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

export default {
  name: 'login',
  data() {
    return {
      data: [],
      dataPic: [],
    };
  },
  created() {
    this.getData();
  },
  methods: {
    async getData() {
      await api
        .get(`api/add_pic/`)
        .then((response) => {
          this.dataPic = response.data;
          console.table(this.dataPic);
        })
        .catch((error) => {
          console.log(error);
        });
      await api
        .get(`api/add/`)
        .then((response) => {
          this.data = response.data;
          console.table(this.data);
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