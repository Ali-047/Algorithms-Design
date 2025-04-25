<script setup lang="ts">
const props = defineProps<Props>();
type Props = {
  placeholder: string;
  width: string;
  type: string;
  error?: string | null;
};
const model = defineModel();
</script>

<template>
  <div class="relative">
    <input
      :class="error ? 'border-red-600!' : model ? 'border-primary!' : ''"
      name="username"
      :type="type"
      placeholder=""
      class="input_text color-primary-700 text-amber-50 peer"
      :style="{ width: props.width }"
      v-model="model"
    />
    <label
      for="username"
      class="input_text_label peer-focus:text-sm! peer-focus:-top-4 transition-all peer-focus:text-primary! peer-placeholder-shown:top-1 peer-placeholder-shown:text-sm"
      :class="
        error
          ? '-top-4 text-red-600!'
          : model
            ? '-top-4 text-primary!'
            : 'top-0'
      "
    >
      {{ props.placeholder }}
    </label>
    <div @click="console.log(model)" class="text-red-600 text-xs" v-if="error">
      {{ error }}
    </div>
  </div>
</template>

<style scoped lang="scss"></style>
