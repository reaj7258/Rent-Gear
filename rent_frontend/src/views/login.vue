<template>
  <div style="height: 100vh">
    <div class="grid grid-cols-5">
      <div class="col-span-3 bg-blue-100"><img class="h-screen w-full" src="@/assets/data.jpg" alt=""></div>
      <div class="col-span-2 h-[100vh] bg-slate-300 px-20">
        <input type="text" v-model="email" class="mt-28 rounded-3xl border-2 border-gray-500 bg-slate-200 placeholder:text-center text-xl py-3 px-10 w-full hover:bg-slate-300" placeholder="Email" />
        <input type="password" v-model="password" class="mt-14 rounded-3xl border-2 border-gray-500 bg-slate-200 placeholder:text-center text-xl py-3 px-10 w-full hover:bg-slate-300" placeholder="Password" />
        <button @click="Submit()" class="mt-14 py-2 px-10 bg-gray-200 rounded-3xl text-xl border-2 border-gray-500 hover:bg-gray-700 hover:text-white">Sign In</button>
        <p class="mt-10"><router-link to="/register" class="text-xl underline hover:text-blue-900 text-gray-600 cursor-pointer">Create One, Sign up</router-link></p>
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
  </div>
</template>

<script>
import api from '../../boot/axios';
import { notify } from 'notiwind';

export default {
  name: 'login',
  data() {
    return {
      email: '',
      password: '',
      varr: false,
    };
  },
  methods: {
    async Submit() {
      await api
        .get(`api/customer/`)
        .then((response) => {
          let a = [];
          a = response.data;
          for (let i = 0; i < a.length; i++) {
            if (a[i].email == this.email && a[i].password == this.password) {
              this.varr = true;
              localStorage.setItem('id', a[i].id);
              localStorage.setItem('name', a[i].firstName + ' ' + a[i].lastName);
              localStorage.setItem('email', a[i].email);
              localStorage.setItem('role', a[i].role);
              if (a[i].role == 1) {
                this.$router.push({ name: 'Home' });
              } else if (a[i].role == 2) {
                this.$router.push({ name: 'My Adds' });
              } else if (a[i].role == 3) {
                this.$router.push({ name: 'Dashboard' });
              }
              break;
            }
          }
          if (this.varr == false) {
            this.toastDanger();
            this.password = '';
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    toastDanger() {
      notify(
        {
          group: 'danger',
          title: 'Sign In Failed',
          text: 'User Credentials Does Not Match',
        },
        1500
      );
    },
  },
};
</script>