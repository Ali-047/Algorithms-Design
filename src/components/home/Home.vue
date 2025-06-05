<script setup lang="ts">
import {onMounted} from "vue";
import HeaderComponents from "./components/HeaderComponents.vue";
import FooterComponents from "./components/FooterComponents.vue";
import AboutUsComponents from "@/components/home/components/AboutUsComponents.vue";
import ContactUsComponents from "@/components/home/components/ContactUsComponents.vue";
import ImageSliderComponents from "@/components/home/components/ImageSliderComponents.vue";

onMounted(() => {
  console.log("in home")
})
</script>

<template>
  <div>
    <header-components/>
    <section id="top"></section>
    <div>
      <image-slider-components/>
      <about-us-components/>
      <contact-us-components/>
    </div>
    <footer-components/>
  </div>
</template>

<style scoped lang="scss">

</style>