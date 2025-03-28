<script setup lang="ts">
import {onMounted} from "vue";
import HeaderComponents from "./components/HeaderComponents.vue";
import FooterComponents from "./components/FooterComponents.vue";

onMounted(() => {
  console.log("in home")
})
</script>

<template>
  <div>
    <header-components/>
    <div style="height:2000px">
    </div>
    <footer-components/>
  </div>
</template>

<style scoped lang="scss">

</style>