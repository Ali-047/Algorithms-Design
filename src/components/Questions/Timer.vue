<script setup>
import {ref, onMounted} from "vue";

let minute = ref(0);
let second = ref(0);

function startTimer() {
  if (second.value === 59) {
    minute.value++;
    second.value = 0;
  }
  second.value++;
}

const interval = setInterval(() => {
  startTimer();
} , 1000)

onMounted(() => {
  startTimer();
})
</script>

<template>
  <div class="text-white">
    <p>
      <span v-if="minute >= 0 && minute < 10">0</span>
      {{ minute }} :
      <span v-if="second >= 0 && second < 10">0</span>
      {{ second }}
    </p>
  </div>
</template>

<style scoped lang="scss">

</style>