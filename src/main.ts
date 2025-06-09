import {createApp} from 'vue'
import App from './App.vue'
import './style.css'
import {registerConfigPlugins} from "./plugins";
import HttpClient from "./api-access";
import ClickOutside from '@/components/authentication/components/ClickOutsideDirective.ts'
import 'vue3-toastify/dist/index.css';

const app = createApp(App)
app.directive('click-outside', ClickOutside);
registerConfigPlugins(app)

HttpClient.initialize()

app.mount('#app')
