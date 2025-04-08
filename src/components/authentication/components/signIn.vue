<script setup lang="ts">

</script>

<template>
  <div class="flex-col">
    <div class="flex flex-col justify-between items-center w-[500px] h-[500px] pb-6">
      <img src="@/assets/loginLogo.svg">
      <filed-input type="text" width="400px" placeholder="userName"/>
      <div class="flex gap-4">
        <filed-input type="password" width="190px" placeholder="password"/>
        <filed-input type="password" width="190px" placeholder="config password"/>
      </div>
      <filed-input type="email" width="400px" placeholder="email"/>
      <div class="flex justify-around">
        <a class="w-fit">
          <div class="buton1">sign up</div>
          <div class="back"></div>
        </a>
      </div>
    </div>
<div class="flex mt-3 mb-9">
  <div class="text-white text-xs flex items-center mx-auto  gap-1">if you have account ?
    <router-link :to="{name:'auth',params:{type:'login'}}">
      <div class="text-primary hover:text-blue-600"> login now</div>
    </router-link>
    .
  </div>
</div>
  </div>
</template>

<style scoped lang="scss">
a {
  color: white;
  position: relative;
}

.buton1 {
  font-weight: 600;
  border-radius: 2em;
  padding: 0.75rem 1.5rem;
  background-color: rgba(255, 255, 255, 0.253);
  backdrop-filter: blur(10px);
  transform: scale(1.1);
  transition: 0.2s ease-in-out;
  z-index: 2;
  position: relative;
}

.back {
  position: absolute;
  background: linear-gradient(20deg, rgb(174, 6, 216) 0%, rgb(85, 31, 200));
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1;
  border-radius: 2em;
  box-shadow: -5px 0 10px rgb(140, 12, 147), 5px 0 10px rgb(85, 31, 200);
  transform: translateY(10px);
}

.buton1:hover {
  transform: translateY(10px);
  box-shadow: -10px 0 50px rgba(241, 0, 108, 0.352),
  10px 0 50px rgb(85, 31, 200);
}

</style>