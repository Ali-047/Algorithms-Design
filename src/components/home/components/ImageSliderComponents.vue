<template>
  <div class="relative w-full max-w-xl mx-auto h-150">
    <!-- دکمه‌های حرکت -->
    <button
        @click="prev"
        class="absolute left-0 top-1/2 transform -translate-y-1/2 bg-gray-700 text-white p-2 rounded-full shadow-lg">
      &lt;
    </button>

    <button
        @click="next"
        class="absolute right-0 top-1/2 transform -translate-y-1/2 bg-gray-700 text-white p-2 rounded-full shadow-lg">
      &gt;
    </button>

    <!-- نمایش عکس‌ها -->
    <div class="overflow-hidden">
      <div class="flex transition-transform duration-500" :style="sliderStyle">
        <img v-for="(image, index) in images"
             :key="index"
             :src="image"
             alt="Slider Image"
             class="w-full object-cover"/>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {ref} from 'vue';
const images = ref<string[]>([
  '@/assets/images/exam.jpg',
  '@/assets/images/exam.jpg',
  '@/assets/images/exam.jpg'
]);

const currentIndex = ref(0);
const totalImages = computed(() => images.value.length);

const next = () => {
  if (currentIndex.value < totalImages.value - 1) {
    currentIndex.value++;
  } else {
    currentIndex.value = 0;
  }
};

const prev = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--;
  } else {
    currentIndex.value = totalImages.value - 1;
  }
};

const sliderStyle = computed(() => {
  return {
    transform: `translateX(-${currentIndex.value * 100}%)`
  };
});
</script>

<style scoped>
/* اگر نیاز به استایل‌های بیشتر داشتید، می‌توانید اینجا اضافه کنید */
</style>
