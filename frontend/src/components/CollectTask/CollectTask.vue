<template>
    <div>
        <v-row align="center" justify="center" class="md6">
            <v-col cols="6">
                <v-card max-height="600" min-height="600" class="card-cl">
                    <v-card-title class="headline">Выберете задачи:</v-card-title>
                    <v-list>
                        <v-list-group
                                v-for="(themes,themesIndex) in tasks"
                                :key="themes.title"
                                v-model="themes.active"
                                no-action
                        >
                            <template v-slot:activator>
                                <v-list-item-content>
                                    <v-list-item-title v-text="themes.title"></v-list-item-title>
                                </v-list-item-content>
                            </template>


                            <template v-for="(task,taskIndex) in themes.list">
                                <v-list-item
                                        :key="task.id"
                                        @click=""
                                >
                                    <v-list-item-action>
                                        <v-icon @click="reloadTast(task.id,themesIndex,taskIndex)">mdi-reload</v-icon>
                                        <v-checkbox v-model="selectedTasks" :value="task.id"></v-checkbox>
                                    </v-list-item-action>
                                    <v-list-item-content>
                                        <v-list-item-title v-text="task.id"></v-list-item-title>
                                        <v-list-item-content v-html="task.text"></v-list-item-content>
                                        <v-img :src="task.image"></v-img>
                                    </v-list-item-content>
                                </v-list-item>
                                <v-divider inset></v-divider>
                            </template>
                        </v-list-group>
                    </v-list>
                </v-card>
            </v-col>
            <v-col cols="6">
                <v-card max-height="600" min-height="600" class="card-cl">
                    <v-card>
                        <v-card-title class="headline">Настройки теста:</v-card-title>
                        <v-divider inset></v-divider>
                        <v-row align="center" justify="center" class="md6">
                            <v-col cols="4">
                                <v-text-field
                                        label="Длительность теста"
                                        v-model="testTimeValue"
                                ></v-text-field>
                            </v-col>
                            <v-col cols="4">
                                <v-select
                                        v-model="selectItem"
                                        :items="items"
                                        item-text="name"
                                        item-value="id"
                                        label="Единицы времени"
                                ></v-select>
                            </v-col>
                        </v-row>
                        <v-divider inset></v-divider>
                    </v-card>
                    <v-card-title class="headline">Выбранные задачи:</v-card-title>
                    <v-list v-for="task in getChooseTasks">
                        <v-list-item
                                :key="task.id"
                                @click=""
                        >
                            <v-list-item-content>
                                <v-list-item-title v-text="task.id"></v-list-item-title>
                                <v-list-item-content v-html="task.text"></v-list-item-content>
                                <v-img :src="task.image"></v-img>
                            </v-list-item-content>
                        </v-list-item>
                        <v-divider inset></v-divider>
                    </v-list>
                </v-card>
            </v-col>
        </v-row>
        <v-btn x-large color="secondary" class="block" @click="goToNextScreen" :disabled="!selectedTasks.length">
            Cформировать
        </v-btn>
    </div>
</template>

<script>
  import { apiHost } from 'src/api/api.utils';
  import showNotify from 'src/helpers/showNotify';
  import getUrl from 'src/helpers/getUrl';

  export default {
    name: 'CollectTask',
    async mounted() {
      const id = this.$route.params.id;
      try {
        const res = await apiHost.get(`/get_discipline_tasks?id=${id}`);
        this.tasks = res.map(tasksConfig => {
          tasksConfig.list = tasksConfig.list.map(task => {
            task.image = getUrl(task.image)
            return task
          });
          return tasksConfig;
        });
      } catch (e) {
        showNotify({
          text: 'Произошла ошибка',
          type: 'error'
        })
      }
    },
    computed: {
      getChooseTasks: function () {
        return this.tasks.map(tasks => tasks.list).flat().filter(task => this.selectedTasks.includes(task.id));
      }
    },
    data() {
      return {
        testTimeValue: 5,
        selectedTasks: [],
        selectItem: {
          name: 'Минут',
          id: 'm',
          toMs: 60000
        },
        items: [{
          name: 'Минут',
          id: 'm',
          toMs: 60000
        }, {
          name: 'Часов',
          id: 'h',
          toMs: 3600000
        }],
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
    },
    methods: {
      reloadTast: async function (taskId, themesIndex, taskIndex) {
        const disc = this.$route.params.id;
        console.log(taskId, disc, themesIndex, taskIndex)
        try {
          const res = await apiHost.get(`/reload_tasks?task=${taskId}&disc=${disc}`);
          this.tasks[themesIndex].list[taskIndex] = res;
        } catch (e) {
          showNotify({
            text: 'Произошла ошибка',
            type: 'error'
          })
        }

      },
      goToNextScreen: function () {
        this.$router.push({
          path: `/collection?params=${JSON.stringify({
            selectedTasks: this.selectedTasks,
            disc: this.$route.params.id,
            time: +this.testTimeValue * (this.selectItem.toMs
                                         ? this.selectItem.toMs
                                         : this.items.find(val => val.id === this.selectItem).toMs)
          })}`
        })
      }
    }
  }
</script>

<style scoped>
    .card-cl {
        overflow-y: scroll;
    }

    .wrap {
        border: 1px solid #333;
        border-radius: 5px;
    }

    .block {
        display: block;
        margin: 0 auto;
    }

</style>
