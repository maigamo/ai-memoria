<template>
  <div class="default-layout">
    <header class="header">
      <div class="container header-content">
        <div class="logo-container">
          <router-link to="/" class="logo">
            <img src="@/assets/logo.svg" alt="AI Memoria" />
            <span>AI Memoria</span>
          </router-link>
        </div>
        
        <div class="nav-container">
          <nav class="main-nav">
            <router-link to="/" class="nav-link">首页</router-link>
          </nav>
        </div>
        
        <div class="user-menu">
          <template v-if="userStore.isAuthenticated">
            <el-dropdown>
              <span class="user-dropdown-link">
                {{ userStore.currentUser?.full_name || userStore.currentUser?.email }}
                <el-icon class="el-icon--right"><arrow-down /></el-icon>
              </span>
              <template #dropdown>
                <el-dropdown-menu>
                  <el-dropdown-item @click="userStore.logout()">退出登录</el-dropdown-item>
                </el-dropdown-menu>
              </template>
            </el-dropdown>
          </template>
          <template v-else>
            <router-link to="/auth/login" class="btn">登录</router-link>
            <router-link to="/auth/register" class="btn btn-primary">注册</router-link>
          </template>
        </div>
      </div>
    </header>
    
    <main class="main-content">
      <div class="container">
        <router-view />
      </div>
    </main>
    
    <footer class="footer">
      <div class="container">
        <p>&copy; {{ new Date().getFullYear() }} AI Memoria</p>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { ArrowDown } from '@element-plus/icons-vue'
import { useUserStore } from '@/stores/userStore'

const userStore = useUserStore()
</script>

<style scoped lang="scss">
.default-layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.header {
  background-color: var(--color-bg);
  border-bottom: 1px solid var(--color-border);
  padding: 16px 0;
  
  .header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .logo-container {
    .logo {
      display: flex;
      align-items: center;
      text-decoration: none;
      color: var(--color-text);
      font-weight: 600;
      font-size: 18px;
      
      img {
        width: 32px;
        height: 32px;
        margin-right: 8px;
      }
    }
  }
  
  .nav-container {
    .main-nav {
      display: flex;
      gap: 16px;
      
      .nav-link {
        color: var(--color-text);
        text-decoration: none;
        padding: 6px 8px;
        border-radius: var(--radius);
        
        &:hover, &.router-link-active {
          color: var(--color-primary);
          background-color: var(--color-bg-secondary);
        }
      }
    }
  }
  
  .user-menu {
    display: flex;
    gap: 12px;
    align-items: center;
    
    .user-dropdown-link {
      cursor: pointer;
      display: flex;
      align-items: center;
    }
  }
}

.main-content {
  flex: 1;
  padding: 24px 0;
}

.footer {
  background-color: var(--color-bg-secondary);
  padding: 24px 0;
  border-top: 1px solid var(--color-border);
  text-align: center;
  color: var(--color-text-secondary);
}
</style> 