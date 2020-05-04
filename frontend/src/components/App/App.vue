<template>
    <div id="app">
        <v-app>
            <div class="overlay" v-if="$store.state.loader.status">
                <h2 class="loader-text">{{$store.state.loader.message}}</h2>
                <v-progress-circular
                        :size="70"
                        :width="7"
                        color="purple"
                        indeterminate
                        class="spinner-loader"
                ></v-progress-circular>
            </div>
            <notifications group="main"></notifications>
            <div>
                <v-toolbar color="primary">
                    <v-spacer></v-spacer>

                    <v-btn v-for="item in getMenuItems()"
                           class="ma-2"
                           :key="item.title"
                           :to="item.href ? item.href : null"
                           @click="item.fn ? item.fn() : null"
                           style=""
                           outlined>
                        <v-icon left>{{ item.icon }}</v-icon>
                        {{ item.title }}
                    </v-btn>

                    <v-spacer></v-spacer>
                </v-toolbar>
            </div>
            <v-content>
                <v-container fluid grid-list-md text-xs-center>
                    <router-view></router-view>
                </v-container>
            </v-content>
            <v-footer color="primary lighten-1"
                      padless>
                <v-row justify="center" no-gutters>
                    <v-col cols="12" class="primary py-4 text-center white--text">&copy;2020 —
                        <strong>BUGuvix</strong></v-col>
                </v-row>
            </v-footer>
        </v-app>
    </div>
</template>

<script>
  export default {
    name: 'App',
    data() {
      return {};
    },
    methods: {
      getMenuItems() {
        return [{
          title: 'Главная',
          href: '/',
          icon: 'fa-home'
        },
          {
            title: 'Личный кабинет',
            href: '/lk',
            icon: 'fa-id-badge'
          }
        ];
      }
    }
  };
</script>

<style scoped>
    .loader-text {
        color: white;
        position: absolute;
        top: 40%;
    }

    .overlay {
        background: rgba(0, 0, 0, 0.4);
        width: 100%;
        height: 100%;
        position: absolute;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 9999;
    }
</style>
