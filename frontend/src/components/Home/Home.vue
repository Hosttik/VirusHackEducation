<template>
    <div>
        <template v-for="classItemes in classes">
            <v-row align="center" justify="center" class="md6">
                <template v-for="classItem in classItemes">
                    <v-col cols="4">
                        <v-card>
                            <v-img
                                    :src="classItem.image"
                                    class="white--text align-end"
                                    gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                                    height="200px"
                            >
                                <v-card-title v-text="classItem.title"></v-card-title>
                            </v-img>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn x-large color="secondary" @click="goTo(classItem.id)">Создать</v-btn>
                                <v-spacer></v-spacer>
                            </v-card-actions>
                        </v-card>
                    </v-col>
                </template>
            </v-row>
        </template>
    </div>
</template>

<script>
  // import startScreen from 'src/assets/start-screen.png';
  import { apiHost } from 'src/api/api.utils';
  import showNotify from 'src/helpers/showNotify';
  import { splitEvery } from 'ramda'
  import getUrl from 'src/helpers/getUrl';


  export default {
    name: 'Home',
    components: {},
    async mounted() {
      try {
        const res = await apiHost.get('/get_disciplines');
        this.classes = splitEvery(2, res.map(item => {
          item.image = getUrl(item.image);
          return item
        }));
      } catch (e) {
        showNotify({
          text: 'Произошла ошибка',
          type: 'error'
        })
      }
    },
    data() {
      return {
        classes: []
      }
    },
    computed: {},
    methods: {
      goTo: function (id) {
        this.$router.push({
          path: `/collect-tasks/${id}`
        })
      }
    }
  };
</script>

<style scoped>
</style>
