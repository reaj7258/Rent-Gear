<template>
  <div style="height: 100vh">
    <div class="grid grid-cols-5">
      <div class="col-span-3 bg-blue-100"></div>
      <div class="col-span-2 h-[100vh] bg-slate-300 px-20">
        <input type="text" v-model="email" class="mt-16 rounded-3xl border-2 border-gray-500 bg-slate-200 placeholder:text-center text-xl py-3 px-10 w-full hover:bg-slate-300" placeholder="Email" />
        <input type="password" v-model="password" class="mt-12 rounded-3xl border-2 border-gray-500 bg-slate-200 placeholder:text-center text-xl py-3 px-10 w-full hover:bg-slate-300" placeholder="Password" />
        <input type="password" v-model="password2" class="mt-12 rounded-3xl border-2 border-gray-500 bg-slate-200 placeholder:text-center text-xl py-3 px-10 w-full hover:bg-slate-300" placeholder="Confirm Password" />
        <input type="text" v-model="name1" class="mt-12 rounded-3xl border-2 border-gray-500 bg-slate-200 placeholder:text-center text-xl py-3 px-10 w-full hover:bg-slate-300" placeholder="First Name" />
        <input type="text" v-model="name2" class="mt-12 rounded-3xl border-2 border-gray-500 bg-slate-200 placeholder:text-center text-xl py-3 px-10 w-full hover:bg-slate-300" placeholder="Last Name" />
        <input type="text" v-model="phone" class="mt-12 rounded-3xl border-2 border-gray-500 bg-slate-200 placeholder:text-center text-xl py-3 px-10 w-full hover:bg-slate-300" placeholder="Phone" />
        <select v-model="type" class="mt-12 text-center rounded-3xl border-2 border-gray-500 bg-slate-200 placeholder:text-center text-xl py-3 px-10 w-full hover:bg-slate-300">
          <option class="text-gray-700" value="" hidden>User Type</option>
          <option class="text-gray-700" :value="2">Provider</option>
          <option class="text-gray-700" :value="3">User</option>
        </select>
        <button @click="Submit()" class="mt-10 py-2 px-10 bg-gray-200 rounded-3xl text-xl border-2 border-gray-500 hover:bg-gray-700 hover:text-white">Sign Up</button>
        <p class="mt-10"><router-link to="/" class="text-xl underline hover:text-blue-900 text-gray-600 cursor-pointer">Already have an account, Sign in</router-link></p>
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
      email: '',
      password: '',
      password2: '',
      name1: '',
      name2: '',
      phone: '',
      type: '',
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
            if (a[i].email == this.email) {
              this.varr = true;
            }
          }
        })
        .catch((error) => {
          console.log(error);
        });
      if (this.varr) {
        this.toastDanger();
      } else {
        if (this.password != this.password2) {
          this.toastDanger2();
        } else {
          console.log(true);
          const a = {
            firstName: this.name1,
            lastName: this.name2,
            phone: this.phone,
            email: this.email,
            password: this.password,
            role: this.type,
          };
          await api
            .post(`api/customer/`, a)
            .then((res) => {
              console.log(res.data);
              this.toast();
              this.email = '';
              this.password = '';
              this.password2 = '';
              this.name1 = '';
              this.name2 = '';
              this.phone = '';
              this.type = '';
            })
            .catch((error) => {
              console.log(error);
            });
        }
      }
      this.varr = false;
    },
    toastDanger() {
      notify(
        {
          group: 'danger',
          title: 'Email already taken',
          text: 'Use a different email',
        },
        1500
      );
    },
    toast() {
      notify(
        {
          group: 'foo',
          title: 'Account created',
          text: 'You can log in now',
        },
        1500
      );
    },
    toastDanger2() {
      notify(
        {
          group: 'danger',
          title: 'Password mismatch',
          text: 'password does not match',
        },
        1500
      );
    },
  },
};
</script>