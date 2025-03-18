<template>
  <div class="home-page">
    <div v-if="userStore.isAuthenticated" class="welcome-section">
      <h1>欢迎回来，{{ userStore.currentUser?.full_name || '用户' }}</h1>
      <p>AI-Memoria 智能记忆管理系统</p>
    </div>
    <div v-else class="hero-section">
      <h1>AI-Memoria 智能记忆管理系统</h1>
      <p>个人知识管理的全新体验</p>
      <div class="hero-actions">
        <router-link to="/auth/register" class="btn btn-primary">立即开始</router-link>
        <router-link to="/auth/login" class="btn">登录</router-link>
      </div>
    </div>
    
    <div class="features-section">
      <h2>主要特性</h2>
      <div class="features-grid">
        <div class="feature-card">
          <el-icon class="feature-icon"><document /></el-icon>
          <h3>多形式内容录入</h3>
          <p>支持文本、图片、音频等多种内容格式</p>
        </div>
        
        <div class="feature-card">
          <el-icon class="feature-icon"><cpu /></el-icon>
          <h3>智能意图识别</h3>
          <p>基于先进AI模型，智能理解您的需求</p>
        </div>
        
        <div class="feature-card">
          <el-icon class="feature-icon"><search /></el-icon>
          <h3>语义检索</h3>
          <p>通过语义搜索，精准找到您需要的内容</p>
        </div>
        
        <div class="feature-card">
          <el-icon class="feature-icon"><connection /></el-icon>
          <h3>在线/离线混合存储</h3>
          <p>本地和云端数据无缝切换，确保数据安全</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useUserStore } from '@/stores/userStore'
import { Document, Cpu, Search, Connection } from '@element-plus/icons-vue'

const userStore = useUserStore()
</script>

<style scoped lang="scss">
.home-page {
  padding: 24px 0;
}

.welcome-section,
.hero-section {
  text-align: center;
  margin-bottom: 48px;
  
  h1 {
    font-size: 32px;
    font-weight: 600;
    margin-bottom: 12px;
    color: var(--color-text);
  }
  
  p {
    font-size: 18px;
    color: var(--color-text-secondary);
    margin-bottom: 24px;
  }
}

.hero-actions {
  display: flex;
  gap: 16px;
  justify-content: center;
  
  .btn {
    padding: 10px 20px;
    font-size: 16px;
  }
}

.features-section {
  margin-top: 64px;
  
  h2 {
    text-align: center;
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 32px;
    color: var(--color-text);
  }
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 24px;
}

.feature-card {
  background-color: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 24px;
  text-align: center;
  transition: all 0.3s ease;
  
  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  }
  
  .feature-icon {
    font-size: 32px;
    color: var(--color-primary);
    margin-bottom: 16px;
  }
  
  h3 {
    font-size: 18px;
    font-weight: 500;
    margin-bottom: 12px;
    color: var(--color-text);
  }
  
  p {
    color: var(--color-text-secondary);
    font-size: 14px;
  }
}
</style> 