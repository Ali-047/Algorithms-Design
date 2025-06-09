<template>
  <div class="w-full flex justify-center">
    <div
      id="header"
      class="z-10 flex bg-black h-22 justify-between px-5 text-white items-center"
      style="transition: 150ms ease-in"
      :class="handelScroll"
    >
      <img src="@/assets/logo.svg" />
      <div class="flex justify-between w-[500px] text-lg items-center">
        <div @click="scrollToElement('home')" id="homeHeader" class="flex gap-2 HBtn">
          <img src="@/assets/icon/home.svg" />
          <div>Home</div>
        </div>
        <div
          @click="scrollToElement('aboutUs')"
          id="aboutUsHeader"
          class="flex gap-2 HBtn"
        >
          <img src="@/assets/icon/abut_us.svg" />
          <div>About Us</div>
        </div>
        <div
          @click="scrollToElement('contactUs')"
          id="contactUsHeader"
          class="flex gap-2 HBtn"
        >
          <img src="@/assets/icon/call.svg" />
          <div>Contact Us</div>
        </div>
        <div
            id="startExamHeader"
          class="flex gap-2 HBtn"
            @click="scrollToElement('startExam')"
        >
          <img src="@/assets/icon/note.svg" />
          <div>Start Exam</div>
        </div>
      </div>
      <div
        v-if="!!userName"
        v-click-outside="
          () => {
            showProfile = false;
          }
        "
        @click="showProfile = !showProfile"
        class="flex gap-2 flex-row me-10"
      >
        <img class="w-4" src="@/assets/icon/user.svg" />
        <div>profile</div>
        <div
          style="background: oklch(14.5% 0 0)"
          v-if="showProfile"
          class="w-[300px] absolute top-[105%] right-10 z-100 rounded-xl"
        >
          <div style="padding: 20px">
            <div class="flex gap-1">
              <div>User name :</div>
              <div>{{ truncateText(userName, 15) }}</div>
            </div>
            <div class="flex gap-1">
              <div>Email :</div>
              <div>{{ truncateText(userEmail, 20) }}</div>
            </div>
          </div>
        </div>
      </div>
      <div
        v-else
        @click="$router.push({ name: 'auth', params: { type: 'login' } })"
        class="me-10 flex gap-2 cursor-pointer"
      >
        <img src="@/assets/icon/login.svg" />
        <div>Log in</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { userData } from "@/stores/userData.ts";
import {AuthenticationApi} from "@/api-access/authenticationApi.ts";
import {jwtDecode} from "jwt-decode";

let isOnTop = ref<boolean>(false);
let selectedId = ref<string>("");
const showProfile = ref<boolean>(false);
const store = userData();
// const userName = ref<string>(store.getUserName);
// const userEmail = ref<string>(store.getUserEmail);
const userName = ref("");
const userEmail = computed(() => store.getUserEmail);
const token = computed(() => localStorage.getItem("token"));

function decodeToken(token) {
  const decodedToken = jwtDecode(token);
  return decodedToken.user_id;
}

function fetchUser(){
  console.log(token.value)
  if (token.value){
    AuthenticationApi.getUserInfo(decodeToken(token.value)).then((res) => {
      console.log(res);
    })
  }
}

onMounted(() => {
  fetchUser()
  window.addEventListener("scroll", () => {
    isOnTop.value = !!window.scrollY;
  });
  observeElement();
});

function observeElement() {
  const targetElement = document.querySelectorAll(".isOnScreen");
  const headerBtn = document.querySelectorAll(".HBtn");
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting && entry.intersectionRatio >= 0.6) {
          selectedId.value = entry.target.id;
          headerBtn.forEach((item) => {
            if (item.id !== selectedId.value + "Header") {
              item.classList.remove("active");
            } else {
              item.classList.add("active");
            }
          });
        }
      });
    },
    {
      root: null,
      threshold: 0.6,
    },
  );

  targetElement.forEach((item) => observer.observe(item));

  onUnmounted(() => {
    observer.disconnect();
  });
}

function truncateText(text: string, maxChars: number = 100) {
  if (!text) return "";
  return text.length > maxChars ? text.slice(0, maxChars) + "..." : text;
}

const handelScroll = computed(() => {
  return isOnTop.value ? "fixed w-[98.5vw] rounded-lg mt-3" : "relative w-full";
});

function scrollToElement(id: string) {
  const element = document.querySelector(`#${id}`);
  if (element) {
    element.scrollIntoView({ behavior: "smooth", block: "end" });
  }
}
</script>

<style scoped lang="scss">
.active {
  background: #3d1066;
  padding: 10px;
  border-radius: 8px;
}

.HBtn {
  cursor: pointer;
}
</style>
