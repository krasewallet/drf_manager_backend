<template>
  <div id="app" style="width:100%;height:100%;">
    <img alt="Vue logo" src="./assets/logo.png" />
    <div style="text-align:left;width:100%;height:70%;">
      <div style="width:35%;height:100%;border: 1px solid gray;float:left;margin-left:3%">
        <textarea style="width:100%;height:100%" v-model="mytext"></textarea>
      </div>
      <div style="float:right;border: 1px solid gray;width:60%;height:100%"><json-viewer :value="myjson" :expand-depth=5></json-viewer></div>
    </div>
  </div>
</template>

<script>
import JsonViewer from 'vue-json-viewer';
import 'vue-json-viewer/style.css';

export default {
  name: 'App',
  components: {
    JsonViewer
  },
  data() {
    return {
      mytext: JSON.stringify({
        id: '5968fcad629fa84ab65a5247',
        firstname: 'Ada',
        lastname: 'Lovelace',
        awards: null,
        known: ['mathematics', 'computing'],
        position: {
          lat: 44.563836,
          lng: 6.495139
        },
        description: `Augusta Ada King, Countess of Lovelace (née Byron; 10 December 1815 – 27 November 1852) was an English mathematician and writer,
        chiefly known for her work on Charles Babbage's proposed mechanical general-purpose computer,
        the Analytical Engine. She was the first to recognise that the machine had applications beyond pure calculation,
        and published the first algorithm intended to be carried out by such a machine.
        As a result, she is sometimes regarded as the first to recognise the full potential of a "computing machine" and the first computer programmer.`,
        bornAt: '1815-12-10T00:00:00.000Z',
        diedAt: '1852-11-27T00:00:00.000Z'
      })
    };
  },
  computed: {
    myjson: function () {
      return JSON.parse(this.mytext)
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
