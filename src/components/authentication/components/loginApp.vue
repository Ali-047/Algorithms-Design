<script setup lang="ts">
import * as yup from 'yup';
import {useField, useForm} from "vee-validate";

type FormValues = {
  username: string;
  password: string;
};
const schema = yup.object({
  username: yup.string().required("You have not entered your username.").min(6, "The username must be at least 6 characters long."),
  password: yup.string().required("Enter your password"),
});


const { handleSubmit,errors ,submitForm} = useForm<FormValues>({
  validationSchema: schema
})
const { value: usernameValue, errorMessage: usernameError } = useField('username')
const { value: passwordValue, errorMessage: passwordError } = useField('password')
const onSubmit = (values: FormValues) => {
  submitForm(values)
  console.log(errors.value)
if (!Object.keys(errors.value).length && !!usernameValue.value && !!passwordValue.value ) {
  alert(`ورود موفق!\nنام کاربری: ${usernameValue.value}\nرمز عبور: ${passwordValue.value}`)
}
}

</script>

<template>
  <div class="flex flex-col w-[500px] h-[500px] items-center pb-6">
    <form @submit.prevent="onSubmit" class="pt-5 pb-8  w-full h-full">
      <div class="flex flex-col justify-between items-center w-full h-full">
        <div class="flex justify-around">
          <img src="@/assets/loginLogo.svg">
        </div>
        <filed-input :error="usernameError" v-model="usernameValue" type="text" width="400px" placeholder="userName"/>
        <filed-input :error="passwordError" v-model="passwordValue" type="password" width="400px" placeholder="password"/>
        <div class="flex justify-around">
          <a  class="w-fit">
            <button type="submit" class="buton1">login</button>
            <div class="back"></div>
          </a>
        </div>
      </div>
    </form>
    <div class="text-white text-xs flex gap-1">Don't have an account ?
      <router-link :to="{name:'auth',params:{type:'signUp'}}">
        <div class="text-primary hover:text-blue-600"> Sign up now</div>
      </router-link>
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