<script setup lang="ts">
import Timer from "@/components/Questions/Timer.vue";
</script>

<template>
  <div class="background flex  justify-around items-center  w-[100vw] h-[100vh]">
    <div class="backgroundShadow w-3/4 h-[75vh] bg-gray opacity-70 rounded-4xl box-border px-10 pt-10">
      <p class="text-white flex justify-between items-center">Question form question one <Timer/></p>
      <textarea
          placeholder="type your answer here"
          class="w-full h-[70%] mt-5 text-white border-2 border-white rounded-2xl box-border px-5 pt-5 resize-none bg-gray-dark"></textarea>
      <div class="w-full h-10 flex items-center justify-center mt-5">
        <button class="bg-primary px-5 py-2 cursor-pointer rounded-lg button text-white" @click="$router.push('/Question')">
          Send Answer
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.background {
  background-image: url('@/assets/bg.jpeg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.background .backgroundShadow {
  box-shadow: -5px 0 20px rgb(140, 12, 147), 5px 0 20px rgb(85, 31, 200);
  animation-name: shadow;
  animation-duration: 2s;
  animation-iteration-count: infinite;
}

@keyframes shadow {
  0% {
    box-shadow: -5px 0 20px rgb(140, 12, 147), 5px 0 20px rgb(85, 31, 200);
  }
  25% {
    box-shadow: 0 5px 20px rgb(140, 12, 147), 0 -5px 20px rgb(85, 31, 200);
  }
  50% {
    box-shadow: 5px 0 20px rgb(140, 12, 147), -5px 0 20px rgb(85, 31, 200);
  }
  100% {
    box-shadow: -5px 0 20px rgb(140, 12, 147), 5px 0 20px rgb(85, 31, 200);
  }
}

.button {
  transition: 100ms ease;
}

.button:hover {
  box-shadow: -5px 0 20px rgb(140, 12, 147), 5px 0 20px rgb(85, 31, 200);
}
</style>