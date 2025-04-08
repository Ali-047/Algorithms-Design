<script setup lang="ts">
const router = useRoute();
console.log(router.params.type);
</script>

<template>
  <!--  <div>hello authentication</div>-->
  <div class="background flex  justify-around items-center  w-[100vw] h-[100vh]">
    <div class=" rounded-2xl  bg-gray-dark flex justify-around items-center">
      <login-app v-if="router.params.type === 'login'"/>
      <sign-in v-else/>
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
</style>