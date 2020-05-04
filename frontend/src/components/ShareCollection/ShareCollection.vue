<template>
    <div>
        <v-overlay v-if="showPopup" light>
            <v-row align="center" justify="center" class="md6">
                <v-col cols="12">
                    <v-card light>
                        <v-card-title class="headline">Ваш результат:{{this.percent}}</v-card-title>
                        <v-btn to="/" class="close">Закрыть</v-btn>
                    </v-card>
                </v-col>
            </v-row>
        </v-overlay>
        <v-row align="center" justify="center" class="md6">
            <v-col cols="6">
                <v-card>
                    <v-card-title class="headline">Задачи:</v-card-title>
                    <v-list v-for="task in tasks">
                        <v-list-item
                                :key="task.id"
                                @click=""
                        >
                            <v-list-item-content>
                                <v-list-item-title v-text="task.id"></v-list-item-title>
                                <v-list-item-content v-html="task.text"></v-list-item-content>
                                <v-img :src="task.image"></v-img>
                                <v-text-field
                                        v-model="task.value"
                                        placeholder="Введите ответ"
                                ></v-text-field>
                            </v-list-item-content>
                        </v-list-item>
                        <v-divider inset></v-divider>
                    </v-list>
                </v-card>
            </v-col>
        </v-row>
        <v-btn x-large color="secondary" class="block" @click="sendTestAnswers">
            Отправить
        </v-btn>
    </div>

</template>

<script>
  import { apiHost } from 'src/api/api.utils';
  import showNotify from 'src/helpers/showNotify';
  import getUrl from 'src/helpers/getUrl';

  export default {
    name: 'ShareCollection',
    async mounted() {
      const params = JSON.parse(this.$route.query.params);
      this.disc = params.disc;
      try {
        const res = await apiHost.get(`/get_selected_tasks?disc=${params.disc}&ids=${params.selectedTasks.join('_')}`);
        this.tasks = res.map(task => {
          task.image = getUrl(task.image);
          return task
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
        tasks: [],
        disc: '',
        showPopup: false,
        percent: 0

      }
    },
    methods: {
      sendTestAnswers: async function () {
        const tasksLength = this.tasks.length;
        const taskAnswers = this.tasks.reduce((res, task) => {
          if (task.value === task.answer) {
            res = res + 1;
          }
          return res;
        }, 0);
        const percentageCompletedTasks = Math.floor(taskAnswers / tasksLength * 100);
        this.percent = percentageCompletedTasks;
        this.showPopup = true;
        await apiHost.get(`/save_result?disc=${this.disc}&path=${this.$router.currentRoute.fullPath}&percent=${percentageCompletedTasks}`);
      }
    }
  }
</script>

<style scoped>
    .close {
        display: flex;
    }

    .block {
        display: block;
        margin: 0 auto;
    }

</style>
