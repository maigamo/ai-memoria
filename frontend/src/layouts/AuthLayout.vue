<template>
  <div class="auth-layout">
    <div class="auth-container">
      <div class="auth-logo">
        <router-link to="/">
          <img src="@/assets/logo.svg" alt="AI Memoria" />
          <h1>AI Memoria</h1>
        </router-link>
      </div>
      
      <div class="auth-card">
        <router-view />
      </div>
      
      <div class="auth-footer">
        <p>&copy; {{ new Date().getFullYear() }} AI Memoria</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// 认证布局组件
</script>

<style scoped lang="scss">
.auth-layout {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--color-bg-secondary);
  padding: 24px 0;
}

.auth-container {
  width: 100%;
  max-width: 420px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.auth-logo {
  margin-bottom: 24px;
  text-align: center;
  
  a {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-decoration: none;
    
    img {
      width: 48px;
      height: 48px;
      margin-bottom: 8px;
    }
    
    h1 {
      color: var(--color-text);
      font-size: 24px;
      font-weight: 500;
      margin: 0;
    }
  }
}

.auth-card {
  width: 100%;
  background-color: var(--color-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 24px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.05);
}

.auth-footer {
  margin-top: 24px;
  color: var(--color-text-secondary);
  font-size: 12px;
}
</style> 