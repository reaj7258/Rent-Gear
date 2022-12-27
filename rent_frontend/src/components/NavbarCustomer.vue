<template>
  <div>
    <Disclosure as="nav" class="bg-gray-900" v-slot="{}">
      <div class="mx-auto px-2 sm:px-6 lg:px-8">
        <div class="relative flex items-center h-2">
          <div class="hidden md:block w-[70vw]">
            <div class="flex-1 flex items-left justify-left sm:items-stretch sm:justify-start">
              <div class="flex-shrink-0 flex items-left">
                <p class="text-2xl text-white font-bold">Rent Gear</p>
              </div>
            </div>
          </div>
          <div class="hidden sm:block sm:ml-6">
            <div class="flex space-x-1 mt-2">
              <a v-for="item in navigation" :key="item.name" :class="[item.current ? 'bg-gray-500 text-white' : 'text-gray-200 hover:bg-gray-700 hover:text-white', 'px-3 py-2 rounded-md font-medium']" :aria-current="item.current ? 'page' : undefined"
                ><router-link :to="item" @click.native="changeActive(item)" style="text-decoration: none; color: inherit">{{ item.name }}</router-link></a
              >
            </div>
          </div>
          <div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
            <!-- Profile dropdown -->
            <Menu as="div" class="ml-3 relative" style="z-index: 1">
              <div>
                <!-- menu image -->
                <MenuButton class="bg-gray-300 flex text-xl rounded-full focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-color2 focus:ring-white">
                  <span class="sr-only">Open user menu</span>
                  <i class="fas fa-user" style="color: white; background-color: "></i>
                  <!-- <img class="h-8 w-8 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="" /> -->
                </MenuButton>
              </div>
              <transition enter-active-class="transition ease-out duration-100" enter-from-class="transform opacity-0 scale-95" enter-to-class="transform opacity-100 scale-100" leave-active-class="transition ease-in duration-75" leave-from-class="transform opacity-100 scale-100" leave-to-class="transform opacity-0 scale-95">
                <template v-if="userSigned == true">
                  <MenuItems class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5 focus:outline-none">
                    <p class="text-sm font-bold">{{ name }} ({{ role }})</p>
                    <hr />

                    <MenuItem v-slot="{ active }">
                      <a href="#" :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700']" @click="logout">Sign out</a>
                    </MenuItem>
                  </MenuItems>
                </template>
                <template v-else>
                  <MenuItems class="origin-top-right absolute right-0 mt-2 w-48 rounded-md shadow-lg py-1 bg-white ring-1 ring-black ring-opacity-5 focus:outline-none">
                    <MenuItem v-slot="{ active }">
                      <a href="/login" :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700']">Sign In</a>
                    </MenuItem>
                  </MenuItems>
                </template>
              </transition>
            </Menu>
          </div>
        </div>
      </div>
    </Disclosure>
  </div>
</template>

<script>
import api from '../../boot/axios';
import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue';

export default {
  name: 'NavbarComponent',
  components: {
    Disclosure,
    DisclosureButton,
    DisclosurePanel,
    Menu,
    MenuButton,
    MenuItem,
    MenuItems,
  },
  data() {
    return {
      name: '',
      message: null,
      useremail: '',
      indx: 0,
      currentuser: [],
      userSigned: true,
      navigation: [],
      role: '',
      lang: '',
    };
  },
  props: ['routepath'],
  created() {
    this.getName();
    if (localStorage.lang) {
      this.lang = localStorage.lang;
    } else {
      this.lang = 'Eng';
    }
  },

  methods: {
    getCurrentTab() {
      let currentTab = localStorage.getItem('current');

      if (currentTab != null) {
        this.navigation.forEach((element) => {
          // console.log('hello');
          // console.log(element);
          if (element.name == currentTab) {
            // console.log('match');
            element.current = true;
          } else {
            element.current = false;
          }
        });
      }
    },
    changeActive(item) {
      this.navigation.forEach((element) => {
        if (element.name == item.name) {
          element.current = true;
          localStorage.setItem('current', element.name);
        } else {
          element.current = false;
        }
      });
    },
    async logout() {
      localStorage.removeItem('email');
      localStorage.removeItem('name');
      localStorage.removeItem('role');

      this.$router.push('/');
    },
    async getName() {
      this.role = localStorage.getItem('role');
      if (this.role == '1') {
        this.role = 'Admin';
      }
      if (this.role == '2') {
        this.role = 'Provider';
      }
      if (this.role == '3') {
        this.role = 'User';
      }
      this.name = localStorage.getItem('name');
      if (this.role == 'Admin') {
        this.navigation = [
          { name: 'Home', to: '#', current: true },
          { name: 'Category Add', to: '/', current: false },
        ];
      } else if (this.role == 'Provider') {
        this.navigation = [
          { name: 'My Adds', to: '#', current: true },
          { name: 'Create Add', to: '/', current: false },
        ];
      } else if (this.role == 'User') {
        this.navigation = [];
      }
      // console.table(this.navigation);
    },
  },
};
</script>

<style scoped>
/* ============ desktop view ============ */
@media all and (min-width: 992px) {
  .dropdown-menu li {
    position: relative;
  }
  .nav-item .submenu {
    display: none;
    position: absolute;
    left: 100%;
    top: -7px;
  }
  .nav-item .submenu-left {
    right: 100%;
    left: auto;
  }
  .dropdown-menu > li:hover {
    background-color: #f1f1f1;
  }
  .dropdown-menu > li:hover > .submenu {
    display: block;
  }
}
/* ============ desktop view .end// ============ */

/* ============ small devices ============ */
@media (max-width: 991px) {
  .dropdown-menu .dropdown-menu {
    margin-left: 0.7rem;
    margin-right: 0.7rem;
    margin-bottom: 0.5rem;
  }
}
/* ============ small devices .end// ============ */
</style>
