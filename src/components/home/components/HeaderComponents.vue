<template>
  <div class="w-full flex justify-center">
    <div id="header" class="flex bg-black  h-22 justify-between px-5 text-white items-center" :class="handelScroll">
      <img src="@/assets/logo.svg">
      <div class="flex justify-between w-[500px]  text-lg items-center">
        <div @click="console.log(isOnTop)" class="flex gap-2">
          <img src="@/assets/icon/home.svg"/>
          <div>Home</div>
        </div>
        <div class="flex gap-2">
          <img src="@/assets/icon/abut_us.svg"/>
          <div>aboutUs</div>
        </div>
        <div class="flex gap-2">
          <img src="@/assets/icon/call.svg"/>
          <div>Contact Us</div>
        </div>
        <div class="flex gap-2">
          <img src="@/assets/icon/note.svg"/>
          <div>Start Exam</div>
        </div>
      </div>
      <div class="me-10 flex gap-2">
        <img src="@/assets/icon/login.svg"/>
        <div>Log in</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {computed, onMounted} from "vue";

let isOnTop = ref<boolean>(false);
onMounted(() => {
  window.addEventListener("scroll", () => {
    isOnTop.value = !!window.scrollY;
  })
})

const handelScroll = computed(() => {
  return isOnTop.value ? "fixed w-[99vw] rounded-lg mt-3" : "relative w-full";
});
</script>

<style scoped lang="scss">

</style>
