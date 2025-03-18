import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
import { VitePWA } from 'vite-plugin-pwa'
import { fileURLToPath, URL } from 'node:url'
import dns from 'node:dns'
import os from 'node:os'

// 使用IPv4
dns.setDefaultResultOrder('ipv4first')

// 获取本机IP地址
function getLocalIP() {
  const networkInterfaces = os.networkInterfaces()
  for (const interfaceName in networkInterfaces) {
    const interfaces = networkInterfaces[interfaceName]
    if (!interfaces) continue
    
    for (const iface of interfaces) {
      // 过滤出IPv4地址并且非内部地址
      if (iface.family === 'IPv4' && !iface.internal) {
        return iface.address
      }
    }
  }
  return '127.0.0.1' // 如果没有找到合适的IP地址，返回localhost
}

const localIP = getLocalIP()

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  // 加载环境变量
  const env = loadEnv(mode, process.cwd())
  
  // 从环境变量获取API地址，如果没有则使用本机IP
  const apiBaseUrl = env.VITE_API_BASE_URL || `http://${localIP}:10012`
  
  return {
    plugins: [
      vue(),
      VitePWA({
        registerType: 'autoUpdate',
        includeAssets: ['favicon.svg', 'logo.svg'],
        manifest: {
          name: 'AI Memoria',
          short_name: 'AI Memoria',
          description: '智能记忆管理系统',
          theme_color: '#ffffff',
          icons: [
            {
              src: 'favicon.svg',
              sizes: '192x192',
              type: 'image/svg+xml'
            },
            {
              src: 'favicon.svg',
              sizes: '512x512',
              type: 'image/svg+xml'
            }
          ]
        }
      })
    ],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    },
    server: {
      host: '0.0.0.0', // 监听所有网络接口
      port: 10011,
      strictPort: false, // 如果端口被占用，尝试下一个可用端口
      proxy: {
        '/api': {
          target: apiBaseUrl,
          changeOrigin: true
        }
      }
    }
  }
}) 