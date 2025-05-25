<!--<script setup lang="ts">-->


<!--</script>-->

<!--<template>-->
<!--  <div class="w-full h-120 mt-20 flex items-center justify-around">-->
<!--    <button class="w-10 h-10 border-2 font-bold cursor-pointer text-white rounded-3xl"> < </button>-->
<!--    <img src="@/assets/images/exam.jpg" alt="" class="w-10/12 h-120 bg-black">-->
<!--    <button class="w-10 h-10 border-2 font-bold cursor-pointer text-white rounded-3xl"> > </button>-->
<!--  </div>-->
<!--</template>-->


<script setup lang="ts">
import { ref, computed, onMounted, onBeforeMount } from 'vue'
import img1 from '@/assets/images/exam.jpg'
import img2 from '@/assets/images/exam2.jpg'

let intervalId: number | undefined

const images = [img1, img2]
const currentIndex = ref(0)
const direction = ref<'left' | 'right'>('right') // جهت حرکت

const currentImage = computed(() => images[currentIndex.value])

function prevImage() {
  direction.value = 'left'
  currentIndex.value = (currentIndex.value - 1 + images.length) % images.length
}

function nextImage() {
  direction.value = 'right'
  currentIndex.value = (currentIndex.value + 1) % images.length
}

onMounted(() => {
  intervalId = setInterval(() => {
    nextImage()
  }, 3500)
})

onBeforeUnmount(() => {
  clearInterval(intervalId)
})

</script>

<template>
  <div class="w-full h-120 mt-20 flex items-center justify-around overflow-hidden">
    <button @click="prevImage" class="w-10 h-10 border-2 font-bold cursor-pointer text-white rounded-3xl hover:bg-white hover:text-black transition"> &lt; </button>

    <Transition
        :name="direction === 'right' ? 'slide-right' : 'slide-left'"
        mode="out-in"
    >
      <img
          :key="currentImage"
          :src="currentImage"
          alt=""
          class="w-10/12 h-120"
      />
    </Transition>

    <button @click="nextImage" class="w-10 h-10 border-2 font-bold cursor-pointer text-white rounded-3xl hover:bg-white hover:text-black transition"> &gt; </button>
  </div>
</template>

<style scoped>
.slide-right-enter-active {
  transition: all 0.5s ease;
  transform: translateX(100%);
  opacity: 0;
}
.slide-right-enter-from {
  transform: translateX(100%);
  opacity: 0;
}
.slide-right-enter-to {
  transform: translateX(0);
  opacity: 1;
}
.slide-right-leave-active {
  transition: all 0.5s ease;
}
.slide-right-leave-to {
  transform: translateX(-100%);
  opacity: 0;
}

/* Slide from left */
.slide-left-enter-active {
  transition: all 0.5s ease;
  transform: translateX(-100%);
  opacity: 0;
}
.slide-left-enter-from {
  transform: translateX(-100%);
  opacity: 0;
}
.slide-left-enter-to {
  transform: translateX(0);
  opacity: 1;
}
.slide-left-leave-active {
  transition: all 0.5s ease;
}
.slide-left-leave-to {
  transform: translateX(100%);
  opacity: 0;
}
</style>
