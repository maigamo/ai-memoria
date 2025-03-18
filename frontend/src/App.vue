<template>
  <div class="app" :data-theme="theme">
    <NetworkStatus v-if="showNetworkStatus" />
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { useLocalStorage } from '@vueuse/core'
import { computed, watchEffect, ref } from 'vue'
import NetworkStatus from '@/components/NetworkStatus.vue'
import { SHOW_NETWORK_STATUS } from '@/config'

// 检测是否为开发环境
const isDevelopment = import.meta.env.MODE === 'development'

// 是否显示网络状态组件（仅在开发环境且配置启用时显示）
const showNetworkStatus = computed(() => isDevelopment && SHOW_NETWORK_STATUS)

// 主题系统 (跟随系统，支持手动切换)
const userTheme = useLocalStorage('theme', 'auto')
const systemDarkMode = window.matchMedia('(prefers-color-scheme: dark)')

const theme = computed(() => {
  if (userTheme.value === 'auto') {
    return systemDarkMode.matches ? 'dark' : 'light'
  }
  return userTheme.value
})

// 同步HTML data-theme属性，用于CSS变量切换
watchEffect(() => {
  document.documentElement.setAttribute('data-theme', theme.value)
})
</script>

<style scoped>
.app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}
</style> 