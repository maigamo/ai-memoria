<template>
  <div class="network-status">
    <h3>网络连接状态</h3>
    <div v-if="loading">
      <p>正在检测连接...</p>
    </div>
    <div v-else-if="connected" class="status connected">
      <p>已连接到后端服务器</p>
      <ul>
        <li><strong>前端地址:</strong> {{ info.clientHost }}:{{ info.clientPort }}</li>
        <li><strong>后端地址:</strong> {{ info.serverHost }}:{{ info.serverPort }}</li>
        <li><strong>API基础URL:</strong> {{ info.baseUrl }}</li>
      </ul>
    </div>
    <div v-else class="status disconnected">
      <p>无法连接到后端服务器</p>
      <p>请检查后端服务是否正常运行，或者检查API配置是否正确</p>
      <ul>
        <li><strong>配置的后端地址:</strong> {{ info.baseUrl }}</li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { getApiInfo } from '@/config';

const info = getApiInfo();
const loading = ref(true);
const connected = ref(false);

// 检测后端连接状态
async function checkConnection() {
  loading.value = true;
  try {
    const response = await fetch(`${info.baseUrl}/api/v1/health-check`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    });
    connected.value = response.ok;
  } catch (error) {
    console.error('连接后端服务器失败:', error);
    connected.value = false;
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  checkConnection();
  // 每30秒检查一次连接状态
  setInterval(checkConnection, 30000);
});
</script>

<style scoped>
.network-status {
  margin: 1rem;
  padding: 1rem;
  border-radius: 0.5rem;
  background-color: #f5f5f5;
}

.status {
  padding: 0.5rem;
  border-radius: 0.25rem;
}

.connected {
  background-color: #d4edda;
  color: #155724;
}

.disconnected {
  background-color: #f8d7da;
  color: #721c24;
}

ul {
  list-style-type: none;
  padding-left: 0.5rem;
}

li {
  margin: 0.25rem 0;
}
</style> 