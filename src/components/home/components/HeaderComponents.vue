<template>
  <div class="w-full flex justify-center">
    <div id="header" class="flex bg-black  h-22 justify-between px-5 text-white items-center" style="transition: 150ms ease-in" :class="handelScroll">
      <img src="@/assets/logo.svg">
      <div class="flex justify-between w-[500px]  text-lg items-center">
        <div @click="console.log(isOnTop)" class="flex gap-2 HBtn">
          <img src="@/assets/icon/home.svg"/>
          <div>Home</div>
        </div>
        <div @click="scrollToElement('aboutUs')" id="aboutUsHeader" class="flex gap-2 HBtn">
          <img src="@/assets/icon/abut_us.svg"/>
          <div>About Us</div>
        </div>
        <div @click="scrollToElement('contactUs')" id="contactUsHeader" class="flex gap-2 HBtn">
          <img src="@/assets/icon/call.svg"/>
          <div>Contact Us</div>
        </div>
        <div
            @click="console.log('-------------------------------------------------------------------------------',selectedId)"
            class="flex gap-2 HBtn">
          <img src="@/assets/icon/note.svg"/>
          <div>Start Exam</div>
        </div>
      </div>
      <div @click="$router.push({name:'auth',params:{type:'login'}})" class="me-10 flex gap-2 HBtn">
        <img src="@/assets/icon/login.svg"/>
        <div>Log in</div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {computed, onMounted} from "vue";

let isOnTop = ref<boolean>(false);
let selectedId = ref<string>('')

onMounted(() => {
  window.addEventListener("scroll", () => {
    isOnTop.value = !!window.scrollY;
  })
  observeElement()
})

function observeElement() {
  const targetElement = document.querySelectorAll('.isOnScreen');
  const headerBtn = document.querySelectorAll('.HBtn')

  const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            selectedId.value = entry.target.id;
            headerBtn.forEach((item) => {
              if (item.id !== selectedId.value+"Header") {
                item.classList.remove('active');
              } else {
                item.classList.add('active');
              }
            })
          }
        });
      },
      {
        root: null,
        threshold: 0.6,
      }
  );
  targetElement.forEach((item) => observer.observe(item))

  onUnmounted(() => {
    observer.disconnect();
  });
}

const handelScroll = computed(() => {
  return isOnTop.value ? "fixed w-[98.5vw] rounded-lg mt-3" : "relative w-full";
});

function scrollToElement(id: string) {
  const element = document.querySelector(`#${id}`);
  if (element) {
    element.scrollIntoView({behavior: 'smooth', block: 'end'});
  }
}

</script>

<style scoped lang="scss">
.active {
  background: #3d1066;
  padding: 10px;
  border-radius: 8px;
}
.HBtn{
  cursor: pointer;
}
</style>
