import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  base: "/IDP/setimo_semestre/oficina/farmework/",
  plugins: [
    react(),
  ],
})
