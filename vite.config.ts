import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import tailwindcss from '@tailwindcss/vite'


// https://vite.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        vueDevTools(),
        AutoImport({
            imports: [
                'vue',
                {
                    'vue-router/auto': ['useRoute', 'useRouter']
                }
            ],
            dts: 'src/auto-imports.d.ts',
            eslintrc: {
                enabled: true
            },
            vueTemplate: true
        }),
        Components({
            dts: 'src/components.d.ts'
        }),
        tailwindcss()

    ],
    server: {
        proxy: {
            '^/api': {
                target: process.env.VITE_API_BASEURL,
                changeOrigin: true,
                secure: false
            }
        }
    },
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url)),
        },
        extensions: [
            '.js',
            '.json',
            '.jsx',
            '.mjs',
            '.ts',
            '.tsx',
            '.vue'
        ]
    }
})