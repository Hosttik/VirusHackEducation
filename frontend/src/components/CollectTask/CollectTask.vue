<template>
    <v-row align="center" justify="center" class="md6">
        <v-col cols="6">
            <v-list>
                <v-list-group
                        v-for="themes in tasks"
                        :key="themes.title"
                        v-model="themes.active"
                        no-action
                >
                    <template v-slot:activator>
                        <v-list-item-content>
                            <v-list-item-title v-text="themes.title"></v-list-item-title>
                        </v-list-item-content>
                    </template>


                    <template v-for="task in themes.list">
                        <v-list-item
                                :key="task.name"
                                @click=""
                        >
                            <v-list-item-action>
                                <v-checkbox v-model="selectedTasks" :value="task.id"></v-checkbox>
                            </v-list-item-action>
                            <v-list-item-content>
                                <v-list-item-title v-text="task.name"></v-list-item-title>
                                <v-img :src="task.img"></v-img>
                                <v-list-item-content v-html="task.text"></v-list-item-content>
                            </v-list-item-content>
                        </v-list-item>
                        <v-divider inset></v-divider>
                    </template>
                </v-list-group>
            </v-list>
        </v-col>
    </v-row>

</template>

<script>
  import startScreen from 'src/assets/start-screen.png';
  import { apiHost } from 'src/api/api.utils';
  import showNotify from 'src/helpers/showNotify';

  export default {
    name: 'СollectTask',
    async mounted() {
      const id = this.$route.params.id;
      try {
        const res = await apiHost.get(`/getTaskForClass?id=${id}`);
        this.classes = res.data.classes;
      } catch (e) {
        showNotify({
          text: 'Произошла ошибка',
          type: 'error'
        })
      }
      console.log(this.$route.params.id)
    },
    data() {
      return {
        selectedTasks: [],
        tasks: [{
          title: 'Производные',
          list: [{
            id: 1,
            name: 'Производные задачка 1',
            text: 'Текст текст <strong>текст</strong> текст Текст текст текст текст Текст текст текст текст Текст текст текст текст',
            img: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSeItSWK4DLZTOlwo0rpdv9Y6Bh1IOeSxX_0hn1XIPjG-oFyTA_&usqp=CAU'
          }, {
            id: 2,
            name: 'Производные задачка 2',
            text: 'Текст текст текст текст Текст текст текст текст Текст текст текст текст Текст текст текст текст',
            img: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSeItSWK4DLZTOlwo0rpdv9Y6Bh1IOeSxX_0hn1XIPjG-oFyTA_&usqp=CAU'
          }, {
            id: 3,
            name: 'Производные задачка 3',
            text: 'Текст текст текст текст Текст текст текст текст Текст текст текст текст Текст текст текст текст',
            img: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSeItSWK4DLZTOlwo0rpdv9Y6Bh1IOeSxX_0hn1XIPjG-oFyTA_&usqp=CAU'
          }]
        }, {
          title: 'Интегралы',
          list: [{
            id: 4,
            name: 'Интегралы задачка 1',
            text: 'Текст текст текст текст Текст текст текст текст Текст текст текст текст Текст текст текст текст',
            img: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSeItSWK4DLZTOlwo0rpdv9Y6Bh1IOeSxX_0hn1XIPjG-oFyTA_&usqp=CAU'
          }, {
            id: 5,
            name: 'Интегралы задачка 2',
            text: 'Текст текст текст текст Текст текст текст текст Текст текст текст текст Текст текст текст текст',
            img: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSeItSWK4DLZTOlwo0rpdv9Y6Bh1IOeSxX_0hn1XIPjG-oFyTA_&usqp=CAU'
          }, {
            id: 6,
            name: 'Интегралы задачка 3',
            text: 'Текст текст текст текст Текст текст текст текст Текст текст текст текст Текст текст текст текст',
            img: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSeItSWK4DLZTOlwo0rpdv9Y6Bh1IOeSxX_0hn1XIPjG-oFyTA_&usqp=CAU'
          }]
        }, {
          title: 'Логарифмы',
          list: [{
            id: 7,
            name: 'Логарифм задачка 1',
            text: 'Текст текст текст текст Текст текст текст текст Текст текст текст текст Текст текст текст текст',
            img: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSeItSWK4DLZTOlwo0rpdv9Y6Bh1IOeSxX_0hn1XIPjG-oFyTA_&usqp=CAU'
          }, {
            id: 8,
            name: 'Логарифм задачка 1',
            text: 'Текст текст текст текст Текст текст текст текст Текст текст текст текст Текст текст текст текст',
            img: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSeItSWK4DLZTOlwo0rpdv9Y6Bh1IOeSxX_0hn1XIPjG-oFyTA_&usqp=CAU'
          }, {
            id: 9,
            name: 'Логарифм задачка 1',
            text: 'Текст текст текст текст Текст текст текст текст Текст текст текст текст Текст текст текст текст',
            img: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSeItSWK4DLZTOlwo0rpdv9Y6Bh1IOeSxX_0hn1XIPjG-oFyTA_&usqp=CAU'
          }]
        }]
      }
    }
  }
</script>

<style scoped>

</style>
