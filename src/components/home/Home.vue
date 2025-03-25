<script setup lang="ts">
import {onMounted} from "vue";
import HeaderComponents from "./components/HeaderComponents.vue";
import FooterComponents from "./components/FooterComponents.vue";

onMounted(() => {
  console.log("in home")
})
</script>

<template>
  <header-components/>
  <div style="text-decoration-color: crimson;font-size: 200px" class="" >hi home</div>
  <footer-components/>
</template>

<style scoped lang="scss">

</style>