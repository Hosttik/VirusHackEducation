<template>
    <v-row align="center" justify="center" class="md6">
        <v-col cols="6">
            <v-card>
                <v-row align="center" justify="center">
                    <v-card-title class="headline">Ссылка на тест для отправки:</v-card-title>
                    <v-col cols="2"></v-col>
                    <v-col cols="5">
                        <v-text-field readonly id="copyLink" v-model="shareUrl"></v-text-field>
                    </v-col>
                    <v-col cols="3">
                        <v-btn @click="copyUrl" color="secondary">
                            <div v-if="!copied">Cкопировать</div>
                            <div v-if="copied">Скопировано</div>
                            <v-icon v-if="!copied"> share</v-icon>
                            <v-icon v-if="copied"> done</v-icon>
                        </v-btn>
                    </v-col>
                    <v-col cols="2"></v-col>
                </v-row>
            </v-card>
        </v-col>
    </v-row>


</template>

<script>
  export default {
    name: 'Collection',
    mounted: function () {
      const params = this.$route.query.params;
      this.shareUrl = `${window.location.origin}/share-collection?params=${params}`;
    },
    data() {
      return {
        copied: false,
        shareUrl: '',
      }
    },
    methods: {
      copyUrl() {
        const input = document.getElementById('copyLink');
        input.focus();
        input.select();
        try {
          document.execCommand('copy');
          this.copied = true;
          window.getSelection().removeAllRanges();
          setTimeout(() => (this.copied = false), 1500);
        } catch (err) {
          this.copied = false;
        }
      },
    }
  }
</script>

<style scoped>
    .share-block {
        border: 1px solid #333;
        box-shadow: #333333;
    }


</style>
