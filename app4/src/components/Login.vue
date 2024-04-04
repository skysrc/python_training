<template>
  <div>
    Username:
    <input type="text" name="username" v-model="username" />
    Password:
    <input type="password" name="password" v-model="password" />
    <button @click="doLogin">Login Now</button>
    {{ username }}
  </div>
</template>
<script>
export default {
  data() {
    return {
      username: "", // twp-way binding
      password: "",
    };
  },
  methods: {
    doLogin() {
      let url = "http://localhost:8001/user/signin";
      let formData = new FormData();
      formData.append("username", this.username);
      formData.append("password", this.password);
      fetch(url, { body: formData, method: "POST" })
      .then(data => data.json())
      .then(json => {
        console.log(json);
        localStorage.setItem("jwt", json.access_token);
      });
    },
  },
};
</script>
<style></style>
