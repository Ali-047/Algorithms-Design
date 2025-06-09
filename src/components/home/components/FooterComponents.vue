<script setup lang="ts"></script>

<template>
  <div class="w-full">
    <svg viewBox="0 0 120 16">
      <defs>
        <filter id="goo">
          <feGaussianBlur in="SourceGraphic" stdDeviation="1" result="blur" />
          <feColorMatrix
            in="blur"
            mode="matrix"
            values="
           1 0 0 0 0
           0 1 0 0 0
           0 0 1 0 0
           0 0 0 13 -9"
            result="goo"
          />
          <xfeBlend in="SourceGraphic" in2="goo" />
        </filter>
        <path
          id="wave"
          d="M 0 10 C 30 10 30 15 60 15 C 90 15 90 10 120 10 C 150 10 150 15 180 15 C 210 15 210 10 240 10 v 7.51 h -240.01 z"
        />
      </defs>

      <use id="wave3" class="wave" xlink:href="#wave" x="0" y="-2"></use>
      <use id="wave2" class="wave" xlink:href="#wave" x="0" y="0"></use>
    </svg>
    <div class="flex flex-col pb-[3rem] pt-[6rem] bg-black text-white">
      <div class="gap-10 flex flex-col">
        <div class="mx-15">
          <div class="w-[300px]">
            <img src="@/assets/logo.svg" class="" />
          </div>
          <div class="w-[800px] mx-4">
            Thank you for visiting our website! If you found it useful or
            enjoyable, consider supporting us by giving a ⭐ on GitHub. Also,
            feel free to share our GitHub with your friends who might be
            interested.
          </div>
        </div>
        <div class="w-full block">
          <div class="w-[95vw] bg-white h-[1px] mx-auto"></div>
        </div>
      </div>
      <div class="flex mx-auto gap-5 mt-5">
        <div class="w-[30px]"><img src="@/assets/icon/instagram.svg" /></div>
        <div class="w-[30px]"><img src="@/assets/icon/discord.svg" /></div>
        <div class="w-[30px]"><img src="@/assets/icon/github.svg" /></div>
        <div class="w-[30px]"><img src="@/assets/icon/telegram.svg" /></div>
      </div>
    </div>

    <!--  <div class="bg-black w-full h-[350px] rounded-t-lg" id="test">-->

    <!--  </div>-->
  </div>
</template>

<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css?family=Lato:400,400i,700");

body {
  font-family: Lato, sans-serif;
  --col-deepblue: #000;
}

footer {
  width: 100vw;
  position: fixed;
  bottom: 0px;
}

footer div {
  background-color: var(--col-deepblue);
  margin: -5px 0px 0px 0px;
  padding: 0px;
  color: #fff;
  text-align: center;
}

svg {
  width: 100%;
  overflow: visible;
}

.wave {
  animation: wave 3s linear;
  animation-iteration-count: infinite;
  fill: #000;
}

.drop {
  fill: var(--col-deepblue);
  xfill: #99000055;
  animation: drop 8.2s linear infinite normal;
  stroke: var(--col-deepblue);
  stroke-width: 0.5;
  transform: translateY(25px);
  transform-box: fill-box;
  transform-origin: 50% 100%;
}

.drop1 {
}

.drop2 {
  animation-delay: 8s;
  animation-duration: 8s;
}

.drop3 {
  animation-delay: -7s;
  animation-duration: 8.4s;
}

.drop4 {
  animation-delay: 6.7s;
}

.drop5 {
  animation-delay: 7.7s;
  animation-duration: 8.1s;
}

.drop6 {
  animation-delay: -7.1s;
  animation-duration: 8.2s;
}

.gooeff {
  filter: url(#goo);
}

#wave2 {
  animation-duration: 10s;
  animation-direction: reverse;
  opacity: 1;
}

#wave3 {
  animation-duration: 12s;
  opacity: 0.6;
}

@keyframes drop {
  0% {
    transform: translateY(25px);
  }
  30% {
    transform: translateY(-10px) scale(0.1);
  }
  30.001% {
    transform: translateY(25px) scale(1);
  }
  70% {
    transform: translateY(25px);
  }
  100% {
    transform: translateY(-10px) scale(0.1);
  }
}

@keyframes wave {
  to {
    transform: translateX(-100%);
  }
}
</style>
