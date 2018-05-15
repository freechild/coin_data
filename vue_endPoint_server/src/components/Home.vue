<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2 v-on:click="toggle_board">{{message}}</h2>
    <ol v-if="seen">
      <li v-for="todo in todos">
        high : {{todo.data.high}}
        <br>
        low : {{todo.data.dayLow}}
        <hr>
      </li>
    </ol>
    <div v-bind="test">

    </div>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import axios from 'axios';
import d3 from 'd3';
import es6 from 'es6-promise';


es6.polyfill();
function ajax(): void {
  axios.get('http://127.0.0.1:8000/websocket/')
  .then((response) => {
    return response;
  })
  .catch( (error) => {
    throw new TypeError(error);
  });
}




export default Vue.extend({
  name: 'HelloWorld',
  props: {
    msg: String,
  },
  data() {
    return{
      message : 'test',
      seen : false,
      todos: [],
    };
  },
  methods: {
    toggle_board(): void {
      const flag: boolean = (this.seen === true) ? false : true;
      this.seen = flag;
    },
    test(): void {
      console.log(0);
    },
  },
  created() {
    axios.get('http://127.0.0.1:8000/websocket/')
    .then((response) => {
      this.todos = response.data.polls;
    })
    .catch( (error) => {
      throw new TypeError(error);
    });
    // console.log('created');
  },

});

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: grid;
  margin: 0 10px;
}

.hello{
  ol{
    margin-right: 10%;
    margin-left: 10%;
    height: 29em;
    overflow: auto;
  }
}

</style>
