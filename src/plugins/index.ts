import type {app} from 'vue'
import pinia from '../stores'
import route from "../router";


export function registerConfigPlugins(app: app): void {
    app
        .use(pinia)
        .use(route)
}