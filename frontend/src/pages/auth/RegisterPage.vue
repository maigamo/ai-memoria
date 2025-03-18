<template>
  <div class="register-page">
    <h2>注册 AI Memoria</h2>
    
    <el-form 
      ref="formRef"
      :model="registerForm" 
      :rules="registerRules"
      @submit.prevent="handleRegister"
      class="register-form"
    >
      <el-form-item prop="email">
        <el-input 
          v-model="registerForm.email"
          placeholder="邮箱地址"
          type="email"
          prefix-icon="Message"
        />
      </el-form-item>
      
      <el-form-item prop="full_name">
        <el-input 
          v-model="registerForm.full_name"
          placeholder="姓名（可选）"
          prefix-icon="User"
        />
      </el-form-item>
      
      <el-form-item prop="password">
        <el-input 
          v-model="registerForm.password"
          placeholder="密码"
          type="password"
          prefix-icon="Lock"
          show-password
        />
      </el-form-item>
      
      <el-form-item prop="confirmPassword">
        <el-input 
          v-model="registerForm.confirmPassword"
          placeholder="确认密码"
          type="password"
          prefix-icon="Lock"
          show-password
        />
      </el-form-item>
      
      <div class="form-actions">
        <el-button 
          type="primary" 
          :loading="userStore.loading"
          @click="handleRegister"
          class="submit-btn"
        >
          注册
        </el-button>
      </div>
    </el-form>
    
    <div class="form-footer">
      <p>已有账号？<router-link to="/auth/login">登录</router-link></p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import { useUserStore } from '@/stores/userStore'
import type { FormInstance, FormRules } from 'element-plus'
import { Message, Lock, User } from '@element-plus/icons-vue'

const userStore = useUserStore()
const formRef = ref<FormInstance>()

const registerForm = reactive({
  email: '',
  full_name: '',
  password: '',
  confirmPassword: ''
})

const validatePass = (rule: any, value: string, callback: any) => {
  if (value === '') {
    callback(new Error('请再次输入密码'))
  } else if (value !== registerForm.password) {
    callback(new Error('两次输入的密码不一致'))
  } else {
    callback()
  }
}

const registerRules = reactive<FormRules>({
  email: [
    { required: true, message: '请输入邮箱地址', trigger: 'blur' },
    { type: 'email', message: '请输入有效的邮箱地址', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 6, message: '密码长度至少为6个字符', trigger: 'blur' }
  ],
  confirmPassword: [
    { required: true, validator: validatePass, trigger: 'blur' }
  ]
})

const handleRegister = async () => {
  if (!formRef.value) return
  
  await formRef.value.validate(async (valid) => {
    if (valid) {
      const { email, password, full_name } = registerForm
      await userStore.register({ email, password, full_name })
    }
  })
}
</script>

<style scoped lang="scss">
.register-page {
  h2 {
    text-align: center;
    margin-bottom: 24px;
    color: var(--color-text);
    font-weight: 500;
  }
  
  .register-form {
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