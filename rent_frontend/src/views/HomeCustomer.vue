<template>
  <div style="height: full">
    <div class="grid grid-cols-6">
      <div class="col-span-1"></div>
      <div class="col-span-4 mt-10">
        <div class="grid grid-cols-2">
          <div v-for="d in data" :key="d" class="col-span-2 box bg-slate-300 rounded-lg shadow-lg p-5 m-5">
            <div class="grid grid-cols-4">
              <div class="col-span-1">
                <img :src="d.pic" class="h-40 w-40" />
              </div>
              <div class="col-span-2 py-5">
                <p class="text-2xl p-1 text-left">Title : {{ d.title }}</p>
                <p class="text-2xl p-1 text-left">Amount : {{ d.amount }}</p>
                <p class="text-2xl p-1 text-left">Description : {{ d.description }}</p>
              </div>
              <div class="col-span-1">
                <button @click.prevent="Delete(d.id)" class="text-black py-1 px-3 rounded-md hover:text-white hover:bg-black text-xl bg-red-400">Delete</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-span-1"></div>
      <NotificationGroup group="danger">
        <div class="fixed inset-0 flex items-start justify-end p-6 px-4 py-6 mt-[85vh] pointer-events-none">
          <div class="w-full max-w-sm">
            <Notification v-slot="{ notifications }" enter="transform ease-out duration-300 transition" enter-from="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-4" enter-to="translate-y-0 opacity-100 sm:translate-x-0" leave="transition ease-in duration-500" leave-from="opacity-100" leave-to="opacity-0" move="transition duration-500" move-delay="delay-300">
              <div class="flex w-full max-w-sm mx-auto mt-4 overflow-hidden bg-white rounded-lg shadow-md" v-for="notification in notifications" :key="notification.id">
                <div class="flex items-center justify-center w-12 bg-red-500">
                  <svg class="w-6 h-6 text-white fill-current" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
                    <path d="M20 3.36667C10.8167 3.36667 3.3667 10.8167 3.3667 20C3.3667 29.1833 10.8167 36.6333 20 36.6333C29.1834 36.6333 36.6334 29.1833 36.6334 20C36.6334 10.8167 29.1834 3.36667 20 3.36667ZM19.1334 33.3333V22.9H13.3334L21.6667 6.66667V17.1H27.25L19.1334 33.3333Z" />
                  </svg>
                </div>

                <div class="px-4 py-2 -mx-3">
                  <div class="mx-3">
                    <span class="font-semibold text-red-500">{{ notification.title }}</span>
                    <p class="text-sm text-gray-600">{{ notification.text }}</p>
                  </div>
                </div>
              </div>
            </Notification>
          </div>
        </div>
      </NotificationGroup>
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
      id: localStorage.getItem('id'),
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
        .get(`api/add/?cus=${this.id}`)
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
            break;
          }
        }
      }
      console.table(this.data);
    },
    async Delete(id) {
      await api
        .delete(`api/add/${id}/`)
        .then((response) => {
          console.table(response.data);
          this.getData();
          this.toastDanger2();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    toastDanger2() {
      notify(
        {
          group: 'danger',
          title: 'Deleted',
          text: 'Category deleted',
        },
        1500
      );
    },
  },
};
</script>