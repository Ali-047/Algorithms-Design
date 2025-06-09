<script setup lang="ts">
import { ref } from "vue";
import router from "@/router";

const startExamSection = ref<HTMLElement | null>(null);

defineExpose({ startExamSection });

function routeStartQuestions(): void {
  const token: string = localStorage.getItem("token");
  if (token) {
    router.push("/home/Question");
  } else {
    router.push("/authentication/login");
  }
}
</script>

<template>
  <section ref="startExamSection"></section>
  <div
    class="w-full h-200 mt-5 flex flex-col text-white isOnScreen"
    id="startExam"
  >
    <div class="ml-20 mt-15">
      <h1 class="font-bold text-4xl leading-tight">Start Exam</h1>
    </div>
    <div class="flex items-center justify-center w-full mt-15">
      <p class="block w-[60%]">
        When the test starts, a number of questions will be displayed to you,
        and you must answer these questions one by one and submit your answer.
        Finally, you will be taken to the cheating check page, and users who
        have learned and cheated will be displayed to you based on their
        similarity percentage.
      </p>
    </div>
    <div class="w-full h-10 flex items-center justify-center mt-15">
      <button
        class="bg-primary px-5 py-2 cursor-pointer rounded-lg button"
        @click="routeStartQuestions"
      >
        Start Exam
      </button>
    </div>
    <div class="w-full mt-10 flex items-center justify-center">
      <img
        class="h-100 w-8/12 block"
        src="../../../assets/images/exam.jpg"
        alt=""
      />
    </div>
  </div>
</template>

<style scoped lang="scss">
.button {
  transition: 100ms ease;
}

.button:hover {
  box-shadow:
    -5px 0 20px rgb(140, 12, 147),
    5px 0 20px rgb(85, 31, 200);
}
</style>
