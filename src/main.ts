import {createApp} from 'vue'
import App from './App.vue'
import './style.css'
import {registerConfigPlugins} from "./plugins";


const app = createApp(App)
registerConfigPlugins(app)


app.mount('#app')
