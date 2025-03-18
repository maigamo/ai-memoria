<template>
  <div class="login-page">
    <h2>登录到 AI Memoria</h2>
    
    <el-form 
      ref="formRef"
      :model="loginForm" 
      :rules="loginRules"
      @submit.prevent="handleLogin"
      class="login-form"
    >
      <el-form-item prop="email">
        <el-input 
          v-model="loginForm.email"
          placeholder="邮箱地址"
          type="email"
          prefix-icon="Message"
        />
      </el-form-item>
      
      <el-form-item prop="password">
        <el-input 
          v-model="loginForm.password"
          placeholder="密码"
          type="password"
          prefix-icon="Lock"
          show-password
        />
      </el-form-item>
      
      <div class="form-actions">
        <el-button 
          type="primary" 
          :loading="userStore.loading"
          @click="handleLogin"
          class="submit-btn"
        >
          登录
        </el-button>
      </div>
    </el-form>
    
    <div class="form-footer">
      <p class="admin-tip">默认管理员: aimemoria@example.com / admin123</p>
      <p>还没有账号？<router-link to="/auth/register">立即注册</router-link></p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import { useUserStore } from '@/stores/userStore'
import type { FormInstance, FormRules } from 'element-plus'
import { Message, Lock } from '@element-plus/icons-vue'

const userStore = useUserStore()
const formRef = ref<FormInstance>()

const loginForm = reactive({
  email: '',
  password: ''
})

const loginRules = reactive<FormRules>({
  email: [
    { required: true, message: '请输入邮箱地址', trigger: 'blur' },
    { type: 'email', message: '请输入有效的邮箱地址', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码长度至少为6个字符', trigger: 'blur' }
  ]
})

const handleLogin = async () => {
  if (!formRef.value) return
  
  await formRef.value.validate(async (valid) => {
    if (valid) {
      await userStore.login(loginForm)
    }
  })
}
</script>

<style scoped lang="scss">
.login-page {
  h2 {
    text-align: center;
    margin-bottom: 24px;
    color: var(--color-text);
    font-weight: 500;
  }
  
  .login-form {
    margin-bottom: 16px;
  }
  
  .form-actions {
    display: flex;
    justify-content: center;
    
    .submit-btn {
      width: 100%;
    }
  }
  
  .form-footer {
    margin-top: 24px;
    text-align: center;
    color: var(--color-text-secondary);
    
    .admin-tip {
      margin-bottom: 8px;
      font-size: 13px;
      color: var(--color-primary);
    }
    
    a {
      color: var(--color-primary);
      text-decoration: none;
      font-weight: 500;
      
      &:hover {
        text-decoration: underline;
      }
    }
  }
}
</style> 