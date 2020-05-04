<template>
    <v-row align="center" justify="center" class="md6">
        <v-col cols="6">
            <v-card>
                <v-row align="center" justify="center" >
                    <v-col cols="6">
                        <v-text-field
                                readonly
                                solo
                                id="copyLink"
                                v-model="shareUrl"
                        ></v-text-field>
                    </v-col>
                    <v-col cols="3">
                        <v-btn @click="copyUrl" color="secondary" x-large>
                            <v-icon v-if="!copied"> share</v-icon>
                            <v-icon v-if="copied"> done</v-icon>
                        </v-btn>
                    </v-col>
                </v-row>
            </v-card>
        </v-col>
    </v-row>


</template>

<script>
  export default {
    name: 'Collection',
    data() {
      return {
        copied: false,
        shareUrl: `${window.location.origin}/lists/hash/`,
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
          setTimeout(() => (this.copied = false), CLEAR_SELECTION_TIMEOUT);
        } catch (err) {
          this.copied = false;
        }
      },
    }
  }
</script>

<style scoped>


</style>
