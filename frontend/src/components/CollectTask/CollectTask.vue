<template>
    <div>
        <v-row align="center" justify="center" class="md6">
            <v-col cols="6">
                <v-card max-height="600" min-height="600" class="card-cl">
                    <v-card-title class="headline">Выберете задачи:</v-card-title>
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
                                        :key="task.id"
                                        @click=""
                                >
                                    <v-list-item-action>
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
        selectedTasks: [],
        tasks: []
      }
    },
    methods: {
      goToNextScreen: function () {
        this.$router.push({
          path: `/collection?params=${JSON.stringify({
            selectedTasks: this.selectedTasks,
            disc: this.$route.params.id
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

    .block {
        display: block;
        margin: 0 auto;
    }

</style>
