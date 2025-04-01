import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  base: "/setimo_semestre/oficina/farmework/",
  plugins: [
    react(),
  ],
})
