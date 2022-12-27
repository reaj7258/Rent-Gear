<template>
  <div style="height: full">
    <div class="grid grid-cols-6">
      <div class="col-span-1"></div>
      <div class="col-span-2 mt-10">
        <div class="md:flex md:items-center my-6 auto-rows-1fr">
          <div class="md:w-2/6">
            <label class="block text-gray-500 font-bold text-right text-2xl pr-4" for="inline-full-name"> Title: </label>
          </div>
          <div class="md:w-4/6">
            <input v-model="title" class="md:flex text-xl appearance-none border-2 border-gray-400 rounded w-4/5 py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-gray-100 focus:border-gray-900" type="text" placeholder="title" />
          </div>
        </div>

        <div class="md:flex md:items-center my-6 auto-rows-1fr">
          <div class="md:w-2/6">
            <label class="block text-gray-500 font-bold text-right text-2xl pr-4" for="inline-full-name"> Amount: </label>
          </div>
          <div class="md:w-4/6">
            <input v-model="amount" class="md:flex text-xl appearance-none border-2 border-gray-400 rounded w-4/5 py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-gray-100 focus:border-gray-900" type="number" placeholder="amount" />
          </div>
        </div>

        <div class="md:flex md:items-center my-6 auto-rows-1fr">
          <div class="md:w-2/6">
            <label class="block text-gray-500 font-bold text-right text-2xl pr-4" for="inline-full-name"> Category: </label>
          </div>
          <div class="md:w-4/6">
            <select v-model="category" class="border-2 border-gray-400 rounded w-4/5 text-xl py-2 px-4 text-gray-700 focus:ring-blue-500 focus:border-blue-500 block p-2.5">
              <option class="text-gray-700" value="" hidden>Description Type</option>
              <option class="text-gray-700" v-for="c in data" :key="c" :value="c.name">{{ c.name }}</option>
            </select>
          </div>
        </div>
      </div>
      <div class="col-span-2 mt-10">
        <div class="md:flex md:items-center my-6 auto-rows-1fr">
          <div class="md:w-2/6">
            <label class="block text-gray-500 font-bold text-right text-2xl pr-4" for="inline-full-name"> Description: </label>
          </div>
          <div class="md:w-4/6">
            <textarea v-model="description" class="md:flex text-xl appearance-none border-2 border-gray-400 rounded w-4/5 py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-gray-100 focus:border-gray-900" type="text" placeholder="description" />
          </div>
        </div>

        <div class="md:flex md:items-center my-6 auto-rows-1fr">
          <div class="md:w-2/6">
            <label class="block text-gray-500 font-bold text-right text-2xl pr-4" for="inline-full-name"> Picture: </label>
          </div>
          <div class="md:w-4/6">
            <input class="md:flex appearance-none w-full py-2 px-4 text-gray-700 leading-tight" type="file" autogrow @change="OnFileUpload1" />
          </div>
        </div>
        <div v-if="pic1Boolean == true" class="md:flex md:items-center my-6 auto-rows-1fr">
          <div class="md:w-2/6"></div>
          <div class="md:w-4/6">
            <input class="md:flex appearance-none w-3/5 py-2 px-4 text-gray-700 leading-tight" type="file" autogrow @change="OnFileUpload2" />
          </div>
        </div>
        <div v-if="pic2Boolean == true" class="md:flex md:items-center my-6 auto-rows-1fr">
          <div class="md:w-2/6"></div>
          <div class="md:w-4/6">
            <input class="md:flex appearance-none w-3/5 py-2 px-4 text-gray-700 leading-tight" type="file" autogrow @change="OnFileUpload3" />
          </div>
        </div>
      </div>
      <div class="col-span-1"></div>
      <div class="col-span-3"></div>
      <div class="col-span-2">
        <button @click="Add()" class="py-1 px-10 bg-gray-200 rounded-xl text-lg border-2 border-gray-500 hover:bg-gray-700 hover:text-white">Add</button>
      </div>
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
      id: localStorage.getItem('id'),
      dataC: [],
      data: [],
      category: '',
      title: '',
      amount: '',
      description: '',
      varr: '',
      pic1Boolean: false,
      pic2Boolean: false,
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
          console.table(this.datac);
        })
        .catch((error) => {
          console.log(error);
        });
      await api
        .get(`api/customer/${this.id}/`)
        .then((response) => {
          this.dataC = response.data;
          console.table(this.dataC);
        })
        .catch((error) => {
          console.log(error);
        });
      console.log(this.id);
    },
    async Add() {
      const a = { title: this.title, amount: this.amount, description: this.description, category: this.category, cus: this.id, phone: this.dataC.phone };
      await api
        .post(`api/add/`, a)
        .then((response) => {
          console.table(response.data);
          this.varr = response.data.id;
          this.category = '';
          this.title = '';
          this.description = '';
          this.amount = '';
          this.pic1Boolean = false;
          this.pic2Boolean = false;
          this.uploadImageHandler();
          this.getData();
          this.toast();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    OnFileUpload1(event) {
      this.pot1 = event.target.files[0];
      this.pic1Boolean = true;
      console.log(this.pot1);
    },
    OnFileUpload2(event) {
      this.pot2 = event.target.files[0];
      this.pic2Boolean = true;
      console.log(this.pot2);
    },
    OnFileUpload3(event) {
      this.pot3 = event.target.files[0];
      console.log(this.pot3);
    },
    async uploadImageHandler() {
      const fd = new FormData();
      if (this.pot1 != undefined) {
        fd.append('pic', this.pot1);
      }
      if (this.pot2 != undefined) {
        fd.append('pic2', this.pot2);
      }
      if (this.pot3 != undefined) {
        fd.append('pic3', this.pot3);
      }
      fd.append('add', this.varr);

      const config = {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      };
      await api.post('api/add_pic/', fd, config).then((res) => {
        console.log('pic upload: ', res.data);
      });
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
          text: 'Add Added',
        },
        1500
      );
    },
  },
};
</script>