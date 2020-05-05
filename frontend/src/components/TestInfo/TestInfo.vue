<template>
    <div>
        <v-overlay v-if="showPopup" light>
            <v-row align="center" justify="center" class="wrap">
                <v-col cols="12">
                    <v-card light>
                        <v-container>
                            <v-card-title class="headline">Заполните форму:</v-card-title>
                            <v-text-field
                                    v-model="title"
                                    :rules="titleRules"
                                    label="Тема аппеляции"
                                    required
                            ></v-text-field>
                            <v-textarea
                                    label="Описание проблемы"
                                    v-model="description"
                                    :rules="descriptionRules"
                                    required
                            ></v-textarea>
                            <v-row align="center" justify="center">
                                <v-col cols="4">
                                    <v-btn @click="closePopup" class="close">Закрыть</v-btn>
                                </v-col>
                                <v-col cols="4">
                                    <v-btn @click="sendAppeal" class="close">Отправить</v-btn>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card>
                </v-col>
            </v-row>
        </v-overlay>
        <v-row align="center" justify="center" class="md6" v-for="resultsPart in results">
            <v-col cols="4" v-for="item in resultsPart">
                <v-card outlined>
                    <v-row align="center" justify="center" class="md6" no-gutters>
                        <v-card-title class="headline">Тест выполнен на: {{item.percent}}%</v-card-title>
                        <v-card-actions>
                            <v-btn @click="again(item.path)">Пройти еще раз</v-btn>
                            <v-btn @click="showPopupMethod">Подать аппеляцию</v-btn>
                        </v-card-actions>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>

<script>
  import { apiHost } from 'src/api/api.utils';
  import showNotify from 'src/helpers/showNotify';
  import { splitEvery } from 'ramda';

  export default {
    name: 'TestInfo',
    async mounted() {
      const disc = this.$route.params.id;
      this.disc = disc;
      try {
        const res = await apiHost.get(`/load_results?disc=${disc}`);
        this.results = splitEvery(3, res);
      } catch (e) {
        showNotify({
          text: 'Произошла ошибка',
          type: 'error'
        })
      }
    },
    data() {
      return {
        showPopup: false,
        title: '',
        titleRules: [v => !!v || 'Тема аппеляции обязательное поле'],
        description: '',
        descriptionRules: [v => !!v || 'Заполните описание'],
        results: []
      }
    },
    methods: {
      sendAppeal: async function() {
        // try {
        //   const res = await apiHost.get(`/send_appeal?disc=${disc}`);
        //   this.results = splitEvery(3, res);
        // } catch (e) {
        //   showNotify({
        //     text: 'Произошла ошибка',
        //     type: 'error'
        //   })
        // }
        this.showPopup = false;
        showNotify({
          text: 'Аппеляция успешно отправлена',
          type: 'success'
        });
      },
      closePopup: function () {
        this.showPopup = false;
      },
      showPopupMethod: function () {
        this.showPopup = true;
      },
      again: function (path) {
        this.$router.push({path});
      }
    }
  }
</script>

<style scoped>
    .close {
        display: flex;
    }

    .wrap {
        width: 500px;
    }

</style>
