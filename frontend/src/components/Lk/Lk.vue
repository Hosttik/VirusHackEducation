<template>
    <div>
        <v-navigation-drawer
                v-model="drawer"
                expand-on-hover
                light
                absolute
        >
            <v-list
                    dense
                    nav
                    class="py-0"
            >
                <v-list-item two-line :class="miniVariant && 'px-0'">
                    <v-list-item-avatar>
                        <img src="https://randomuser.me/api/portraits/men/81.jpg">
                    </v-list-item-avatar>

                    <v-list-item-content>
                        <v-list-item-title>Имя</v-list-item-title>
                        <v-list-item-subtitle>Класс</v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>

                <v-divider></v-divider>

                <v-list-item
                        v-for="item in items"
                        :key="item.title"
                        :to="item.href"
                        link
                >
                    <v-list-item-icon>
                        <v-icon>{{ item.icon }}</v-icon>
                    </v-list-item-icon>

                    <v-list-item-content>
                        <v-list-item-title>{{ item.title }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>

        </v-navigation-drawer>
        <v-row align="center" justify="center" class="md6"><h1>Статистика по тестам:</h1></v-row>
        <v-row align="center" justify="center" class="md6">
            <v-col cols="3" v-for="item in results">
                <v-card>
                    <v-img
                            :src="item.image"
                            class="white--text align-end"
                            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                            height="200px"
                    >
                        <v-card-title v-text="item.name"></v-card-title>
                    </v-img>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn x-large color="secondary" :to="`/lk/tests-info/${item.disc}`">Подробнее</v-btn>
                        <v-spacer></v-spacer>
                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>

<script>
  import { apiHost } from 'src/api/api.utils';
  import showNotify from 'src/helpers/showNotify';
  import getUrl from 'src/helpers/getUrl';

  export default {
    name: 'Lk',
    async mounted() {
      try {
        const res = await apiHost.get('get_results');
        this.results = res.map(item=>{
          item.image = getUrl(item.image);
          return item;
        });
      } catch (e) {
        showNotify({
          text: 'Произошла ошибка',
          type: 'error'
        })
      }
    },
    data() {
      return {
        drawer: true,
        miniVariant: true,
        results: [],
        items: [{
          title: 'Новые тесты',
          icon: 'fa-bell',
          href: '/new-tests'
        }, {
          title: 'Решенные тесты',
          icon: 'fa-th-list',
          href: '/tests-history'
        },]
      }
    }
  }
</script>

<style scoped>

</style>
