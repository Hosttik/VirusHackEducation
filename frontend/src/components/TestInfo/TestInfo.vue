<template>
    <div>
        <v-row align="center" justify="center" class="md6" v-for="resultsPart in results">
            <v-col cols="4" v-for="item in resultsPart">
                <v-card outlined>
                    <v-row align="center" justify="center" class="md6" no-gutters>
                        <v-card-title class="headline">Тест выполнен на: {{item.percent}}%</v-card-title>
                        <v-card-actions>
                            <v-btn @click="again(item.path)">Пройти еще раз</v-btn>
                            <v-btn>Подать аппеляцию</v-btn>
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
        results: []
      }
    },
    methods: {
      again: function (path) {
        this.$router.push({path});
      }
    }
  }
</script>

<style scoped>

</style>
