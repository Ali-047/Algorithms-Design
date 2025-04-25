<script setup lang="ts">
import * as yup from 'yup';
import {useField, useForm} from "vee-validate";

type FormValues = {
  username: string;
  password: string;
  email: string;
  configPassword: string;
};
const schema = yup.object({
  username: yup.string().required("You have not entered your username.").min(6, "The name must be at least 6 characters long."),
  password: yup.string().min(8,"The password must be at least 8 characters long.").required("Enter your password"),
  email: yup.string().required().email("Please enter a valid email address."),
  configPassword: yup.string().oneOf([yup.ref('password')], 'Please enter a valid password'),
});


const {handleSubmit, errors,submitForm} = useForm<FormValues>({
  validationSchema: schema
})
const {value: usernameValue, errorMessage: usernameError} = useField('username')
const {value: passwordValue, errorMessage: passwordError} = useField('password')
const {value: emailValue, errorMessage: emailError} = useField('email')
const {value: configPasswordValue, errorMessage: configPasswordError} = useField('configPassword')
const onSubmit = (values: FormValues) => {
  console.log(errors.value)
submitForm(values)
  if (!Object.keys(errors.value).length && !!usernameValue.value && !!passwordValue.value && !!emailValue.value  ) {
    alert(`ورود موفق!\nنام کاربری: ${usernameValue.value}\nرمز عبور: ${passwordValue.value}`)

  }
}

</script>

<template>
  <div class="flex-col">
    <div class="flex flex-col justify-between items-center w-[500px] h-[500px] pb-6 pt-6">
      <img src="@/assets/loginLogo.svg">
      <form  @submit.prevent="onSubmit" class="h-full flex flex-col justify-between items-center">
        <filed-input type="text" width="400px" v-model="usernameValue" :error="usernameError" placeholder="userName"/>
        <div class="flex gap-4">
          <filed-input type="password" width="190px" v-model="passwordValue" :error="passwordError"
                       placeholder="password"/>
          <filed-input type="password" width="190px" placeholder="config password" v-model="configPasswordValue" :error="configPasswordError"/>
        </div>
        <filed-input v-model="emailValue" :error="emailError" type="email" width="400px" placeholder="email"/>
        <div class="flex justify-around">
          <a class="w-fit">
            <button type="submit" class="buton1">sign up</button>
            <div class="back"></div>
          </a>
        </div>
      </form>
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