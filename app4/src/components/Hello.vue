<template>
  <div>
    <h1>Hello World</h1>
    <button @click="doClick">Click Me</button>
    <button @click="doFetch">Click Me</button>
    <ul>
        <li v-for="(event, index) in events" v-bind:key="index">
            Title : {{ event.title }} <br>
            Description : {{ event.description }}
        </li>
    </ul>
  </div>
</template>

<script>
export default {
    data() {
            return {
                events:[]
            }
    },
    methods: {
        doClick() {
            alert("You clicked me");
        },
        doFetch() {
            // this will call the API
            fetch("http://localhost:8001/event/")
              .then((data) => data.json())
              .then((json) => {
                console.log(json)
                // this.events = json;
                this.events.push(...json)
            });
        }
    }
};
</script>

<style>
h1 {
  color: red;
}
</style>
