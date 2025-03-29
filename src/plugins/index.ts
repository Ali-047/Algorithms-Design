import pinia from '../stores'
import route from "../router";
import type {App} from "vue";


export function registerConfigPlugins(app:App): void {
    app
        .use(pinia)
        .use(route)
}