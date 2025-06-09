<script setup>
import { onMounted, ref, reactive } from "vue";
import Timer from "@/components/Questions/Timer.vue";
import { questionApi } from "@/api-access/questionsApi.js";
import { AuthenticationApi } from "@/api-access/authenticationApi.js";
import { jwtDecode } from "jwt-decode";
import router from "@/router/index.js";

const token = localStorage.getItem("token");
const username = ref("");

const questionInfo = reactive({
  all_questions: null,
  name: null,
  num_of_question: null,
  text: null,
});

const answer = reactive({
  username: null,
  question: null,
  text_answer: "",
});

async function getUserInfo() {
  const decoded = jwtDecode(token);
  AuthenticationApi.getUserInfo(decoded.user_id).then((response) => {
    username.value = response.username;
    console.log(username.value);
  });
}

async function fetchQuestions() {
  questionApi.getQuestions({}).then((response) => {
    Object.assign(questionInfo, response.question);
  });
}

async function sendAnswer() {
  answer.username = username.value;
  answer.question = questionInfo.name;
  questionApi.sendUserAnswer(answer).then((response) => {
    if (response.question.message) {
      router.push("/home");
    } else {
      Object.assign(questionInfo, response.question);
    }
  });
}

onMounted(async () => {
  await getUserInfo();
  await fetchQuestions();
});
</script>

<template>
  <div class="background flex justify-around items-center w-[100vw] h-[100vh]">
    <div
      class="backgroundShadow w-3/4 h-[75vh] bg-gray opacity-70 rounded-4xl box-border px-10 pt-10"
    >
      <p class="text-white flex justify-between items-center">
        {{ questionInfo.text }}
        <Timer />
      </p>
      <textarea
        v-model="answer.text_answer"
        placeholder="type your answer here"
        class="w-full h-[70%] mt-5 text-white border-2 border-white rounded-2xl box-border px-5 pt-5 resize-none bg-gray-dark"
      ></textarea>
      <div class="w-full h-10 flex items-center justify-center mt-5">
        <button
          class="bg-primary px-5 py-2 cursor-pointer rounded-lg button text-white"
          @click="sendAnswer"
        >
          Send Answer
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.background {
  background-image: url("@/assets/bg.jpeg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.background .backgroundShadow {
  box-shadow:
    -5px 0 20px rgb(140, 12, 147),
    5px 0 20px rgb(85, 31, 200);
  animation-name: shadow;
  animation-duration: 2s;
  animation-iteration-count: infinite;
}

@keyframes shadow {
  0% {
    box-shadow:
      -5px 0 20px rgb(140, 12, 147),
      5px 0 20px rgb(85, 31, 200);
  }
  25% {
    box-shadow:
      0 5px 20px rgb(140, 12, 147),
      0 -5px 20px rgb(85, 31, 200);
  }
  50% {
    box-shadow:
      5px 0 20px rgb(140, 12, 147),
      -5px 0 20px rgb(85, 31, 200);
  }
  100% {
    box-shadow:
      -5px 0 20px rgb(140, 12, 147),
      5px 0 20px rgb(85, 31, 200);
  }
}

.button {
  transition: 100ms ease;
}

.button:hover {
  box-shadow:
    -5px 0 20px rgb(140, 12, 147),
    5px 0 20px rgb(85, 31, 200);
}
</style>
