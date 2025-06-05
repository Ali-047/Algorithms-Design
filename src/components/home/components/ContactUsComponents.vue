<script setup lang="ts">
import { ref } from 'vue';

const contactUsSection = ref<HTMLElement | null>(null);

defineExpose({ contactUsSection });
</script>

<template>
  <section ref="contactUsSection" id="contact-us"></section>
  <div class="w-full  h-190 grid grid-cols-2 gap-15 justify-items-center text-white">
    <div class="flex flex-col">
      <div class="ml-20">
        <h1 class="font-bold text-4xl leading-tight">
          Contact Us
        </h1>
      </div>
      <div class="ml-20 mt-10">
        <p>
          In this section you can see the ways to contact the developers of this website. <br>
          Our ways of communication are GitHub, Telegram and Instagram.
        </p>
      </div>
      <div class="grid grid-cols-2 mt-15 gap-15 w-full box-border px-15">
        <div>
          <h2 class="text-3xl mb-5">Pedram Aminian</h2>
          <div class="flex gap-5">
            <a href="">
              <img src="../../../assets/icon/github.svg" alt="" class="w-[30px] hover:shadow-white" />
            </a>
            <a href="">
              <img src="../../../assets/icon/telegram.svg" alt="" class="w-[30px]">
            </a>
            <a href="">
              <img src="../../../assets/icon/instagram.svg" alt="" class="w-[30px]">
            </a>
          </div>
        </div>
        <div>
          <h2 class="text-3xl mb-5">Mohammad yousef Rezaei</h2>
          <div class="flex gap-5">
            <a href="">
              <img src="../../../assets/icon/github.svg" alt="" class="w-[30px]">
            </a>
            <a href="">
              <img src="../../../assets/icon/telegram.svg" alt="" class="w-[30px]">
            </a>
            <a href="">
              <img src="../../../assets/icon/instagram.svg" alt="" class="w-[30px]">
            </a>
          </div>
        </div>
        <div>
          <h2 class="text-3xl mb-5">Ali Nemati</h2>
          <div class="flex gap-5">
            <a href="">
              <img src="../../../assets/icon/github.svg" alt="" class="w-[30px]">
            </a>
            <a href="">
              <img src="../../../assets/icon/telegram.svg" alt="" class="w-[30px]">
            </a>
            <a href="">
              <img src="../../../assets/icon/instagram.svg" alt="" class="w-[30px]">
            </a>
          </div>
        </div>
        <div>
          <h2 class="text-3xl mb-5">Amir Reza Ghorbani</h2>
          <div class="flex gap-5">
            <a href="">
              <img src="../../../assets/icon/github.svg" alt="" class="w-[30px]">
            </a>
            <a href="">
              <img src="../../../assets/icon/telegram.svg" alt="" class="w-[30px]">
            </a>
            <a href="">
              <img src="../../../assets/icon/instagram.svg" alt="" class="w-[30px]">
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class="mt-15">
      <img src="../../../assets/images/exam2.jpg" alt="">
    </div>
  </div>
</template>

<style scoped lang="scss">

</style>