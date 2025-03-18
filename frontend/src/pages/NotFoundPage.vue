<template>
  <div class="not-found-page">
    <div class="not-found-content">
      <h1>404</h1>
      <h2>页面未找到</h2>
      <p>您访问的页面不存在或已被移除</p>
      <router-link to="/" class="btn btn-primary">返回首页</router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
// 404 页面组件
</script>

<style scoped lang="scss">
.not-found-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 70vh;
  text-align: center;
}

.not-found-content {
  max-width: 400px;
  
  h1 {
    font-size: 72px;
    font-weight: 700;
    color: var(--color-primary);
    margin-bottom: 8px;
  }
  
  h2 {
    font-size: 28px;
    font-weight: 500;
    color: var(--color-text);
    margin-bottom: 16px;
  }
  
  p {
    font-size: 16px;
    color: var(--color-text-secondary);
    margin-bottom: 24px;
  }
  
  .btn {
    padding: 10px 20px;
    font-size: 16px;
  }
}
</style> 