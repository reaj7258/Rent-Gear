<template>
  <div style="height: full">
    <div class="grid grid-cols-5">
      <div class="col-span-1"></div>
      <div class="col-span-2 mt-10">
        <input type="text" v-model="category" class="rounded-xl border-2 border-gray-500 bg-slate-200 placeholder:text-center text-xl py-2 px-10 w-full hover:bg-slate-300" placeholder="Category" />
      </div>
      <div class="col-span-1 mt-10">
        <button @click="Add()" class="py-2 px-10 bg-gray-200 rounded-xl text-xl border-2 border-gray-500 hover:bg-gray-700 hover:text-white">Add</button>
      </div>
      <div class="col-span-1"></div>
      <div class="col-span-1"></div>
      <div class="col-span-3 mt-10">
        <table class="w-full text-sm text-left text-gray-500">
          <thead class="text-xs text-white uppercase bg-gray-800">
            <tr>
              <th scope="col" class="md:pl-20 px-6 py-3">Category</th>
              <th scope="col" class="px-6 py-3">Remove</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(p, index) in data" :key="index" class="border-b odd:bg-white even:bg-gray-50 text-xl">
              <td class="px-6 py-4 md:pl-20">
                {{ p.name }}
              </td>
              <td class="px-6 py-4">
                <button @click.prevent="Delete(p.name)" class="text-red-900 hover:text-red-500 text-2xl"><i class="fa-solid fa-xmark"></i></button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="col-span-1"></div>
    </div>
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
    <NotificationGroup group="foo">
      <div class="fixed inset-0 flex items-start justify-end px-4 py-6 mt-[85vh] pointer-events-none">
        <div class="w-full max-w-sm">
          <Notification v-slot="{ notifications }" enter="transform ease-out duration-300 transition" enter-from="translate-y-2 opacity-0 sm:translate-y-0 sm:translate-x-4" enter-to="translate-y-0 opacity-100 sm:translate-x-0" leave="transition ease-in duration-500" leave-from="opacity-100" leave-to="opacity-0" move="transition duration-500" move-delay="delay-300">
            <div class="flex w-full max-w-sm mx-auto mt-4 overflow-hidden bg-white rounded-lg shadow-md" v-for="notification in notifications" :key="notification.id">
              <div class="flex items-center justify-center w-12 bg-blue-500">
                <svg class="w-6 h-6 text-white fill-current" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
                  <path d="M20 3.33331C10.8 3.33331 3.33337 10.8 3.33337 20C3.33337 29.2 10.8 36.6666 20 36.6666C29.2 36.6666 36.6667 29.2 36.6667 20C36.6667 10.8 29.2 3.33331 20 3.33331ZM16.6667 28.3333L8.33337 20L10.6834 17.65L16.6667 23.6166L29.3167 10.9666L31.6667 13.3333L16.6667 28.3333Z" />
                </svg>
              </div>

              <div class="px-4 py-2 -mx-3">
                <div class="mx-3">
                  <span class="font-semibold text-button">{{ notification.title }}</span>
                  <p class="text-sm text-gray-600">{{ notification.text }}</p>
                </div>
              </div>
            </div>
          </Notification>
        </div>
      </div>
    </NotificationGroup>
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
      category: '',
    };
  },
  created() {
    this.getData();
  },
  methods: {
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
    async Delete(id) {
      await api
        .delete(`api/category/${id}/`)
        .then((response) => {
          console.table(response.data);
          this.getData();
          this.toastDanger2();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async Add() {
      console.log(this.category);
      let b = false;
      for (let i = 0; i < this.data.length; i++) {
        if (this.data[i].name == this.category) {
          this.toastDanger();
          this.category = '';
          b = true;
        }
      }
      if (b == false) {
        await api
          .post(`api/category/`, { name: this.category })
          .then((response) => {
            console.table(response.data);
            this.category = '';
            this.getData();
            this.toast();
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    toastDanger() {
      notify(
        {
          group: 'danger',
          title: 'Already exist',
          text: 'Use a different category',
        },
        1500
      );
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
    toast() {
      notify(
        {
          group: 'foo',
          title: 'Added',
          text: 'Category Added',
        },
        1500
      );
    },
  },
};
</script>