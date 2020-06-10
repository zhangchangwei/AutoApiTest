<template>
  <div id="Subnet" >
    <router-view/>
  </div>
</template>

<script>
import Login from './components/login.vue'
// export default {
//   name: 'App'
// }
export default {
  components: {
    Login
  },
 }
</script>

<style>
#Subnet {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
