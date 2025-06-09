import { defineStore } from "pinia";
export  const  userData =  defineStore("userData", {
  state: () => {
    return {
      userName : "",
      email : ""
    }
  },
  actions: {
    setUserName(userName:string){
      this.userName = userName
    },
    setEmail(email:string){
      this.email = email
    },
  },
  getters: {
    getUserName(state){
      return state.userName
    },
    getUserEmail(state){
      return state.email
    }
  }
})