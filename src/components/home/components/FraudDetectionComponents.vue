<script setup>
import { onMounted, reactive } from "vue";
import { fraudDetectionApi } from "@/api-access/fraudDetectionApi.js";

let frauds = reactive({});

async function fetchFraudDetections() {
  fraudDetectionApi.getFraudDetection({}).then((response) => {
    Object.assign(frauds, response);
  });
  console.log(frauds);
}

onMounted(async () => {
  await fetchFraudDetections();
});
</script>

<template>
  <div class="w-full h-190 flex items-center justify-center">
    <div
      class="backgroundShadow w-9/12 h-full rounded-3xl box-border px-10 pt-10"
    >
      <h1 class="text-white text-3xl">Live Fraud Detection</h1>
      <div class="scrollbar w-[85%] h-[60%] mx-auto mt-15 overflow-y-auto">
        <div
          style="border: 2px solid #9333ea"
          class="w-full h-[20%] my-5 rounded-2xl flex align-center justify-center text-3xl"
          v-for="(fraud, index) in frauds"
          :key="index"
        >
          <div class="flex items-center justify-around w-full">
            <h3 class="text-primary block text-2xl">
              {{ index }}
              <span class="text-red-700" v-if="fraud > 30">have cheated</span
              ><span class="text-green-700" v-else>did not cheated</span>
            </h3>
            <h3 class="text-primary text-2xl">
              Similarity Percentage :
              <span :class="fraud > 30 ? 'text-red-700' : 'text-blue-500'">{{fraud}}</span>
            </h3>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.scrollbar::-webkit-scrollbar {
  width: 10px;
  height: 10px;
}

.scrollbar::-webkit-scrollbar-track {
  background: #0F0F0F;
  border-radius: 20px;
  margin-bottom: 5vh;
  margin-top: 5vh;
}

.scrollbar::-webkit-scrollbar-thumb {
  background: #bbbbbb;
  border-radius: 20px;
}

.scrollbar::-webkit-scrollbar-thumb:hover {
  background: gray;
}
</style>
