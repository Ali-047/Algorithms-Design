import {createApp} from 'vue'
import App from './App.vue'
import './style.css'
import {registerConfigPlugins} from "./plugins";
import HttpClient from "./api-access";


const app = createApp(App)
registerConfigPlugins(app)

HttpClient.initialize()

app.mount('#app')
