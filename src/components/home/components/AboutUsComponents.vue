<script setup lang="ts"></script>

<template>
  <div
    class="w-full h-250 mt-5 flex flex-col text-white isOnScreen"
    id="aboutUs"
  >
    <div class="ml-20 mt-15">
      <h1 class="font-bold text-4xl leading-tight">About Us</h1>
    </div>
    <div class="flex items-center justify-center w-full mt-15">
      <p class="block w-[40%]">
        This website was designed and coded by a team of four to detect cheating
        in different exams, which works with different cheating detection
        algorithms. You will get to know the members of this team below.
      </p>
    </div>
    <div class="flex items-center justify-center w-full mt-10">
      <img class="h-100" src="@/assets/images/exam.jpg" alt="" />
    </div>
    <div
      class="grid grid-cols-4 justify-items-center mt-10 gap-10 w-full box-border px-15"
    >
      <div>
        <h2 class="text-3xl mb-5">Pedram Aminian</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquid
          consequatur culpa cum dignissimos distinctio enim, error est impedit
          iste, iure labore magnam obcaecati optio quia quis rem repellat sit
          suscipit.
        </p>
      </div>
      <div>
        <h2 class="text-3xl mb-5">Mohammad yousef Rezaei</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus
          accusantium adipisci alias aut dignissimos ea ex, expedita id, illum
          ipsum iste iure maiores maxime minus modi omnis optio sit vero?
        </p>
      </div>
      <div>
        <h2 class="text-3xl mb-5">Ali Nemati</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad assumenda
          fuga modi nam repellendus. Animi cumque, dicta ducimus ea earum
          impedit nesciunt nihil pariatur quo repudiandae sequi sit unde
          voluptatem.
        </p>
      </div>
      <div>
        <h2 class="text-3xl mb-5">Amir Reza Ghorbani</h2>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ad amet
          consequuntur dolor eius esse et, eum fuga illo minima minus officia
          praesentium, quas quasi recusandae repudiandae veniam? Reprehenderit,
          soluta!
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss"></style>
