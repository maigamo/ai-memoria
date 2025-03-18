import { defineStore } from 'pinia'
import { authApi, userApi } from '@/utils/api'
import type { User, UserLogin, UserRegister } from '@/types/api'
import router from '@/router'
import { ElMessage } from 'element-plus'

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null as User | null,
    token: localStorage.getItem('token') || '',
    loading: false,
  }),
  
  getters: {
    isAuthenticated: (state) => !!state.token,
    currentUser: (state) => state.user,
  },
  
  actions: {
    // 登录
    async login(credentials: UserLogin) {
      try {
        this.loading = true
        const { access_token, token_type } = await authApi.login(credentials)
        this.token = access_token
        localStorage.setItem('token', access_token)
        
        // 获取用户信息
        await this.fetchCurrentUser()
        
        ElMessage.success('登录成功')
        router.push('/')
      } catch (error) {
        console.error('登录失败', error)
      } finally {
        this.loading = false
      }
    },
    
    // 注册
    async register(registerData: UserRegister) {
      try {
        this.loading = true
        await authApi.register(registerData)
        ElMessage.success('注册成功，请登录')
        router.push('/auth/login')
      } catch (error) {
        console.error('注册失败', error)
      } finally {
        this.loading = false
      }
    },
    
    // 获取当前用户信息
    async fetchCurrentUser() {
      try {
        if (!this.token) return
        this.loading = true
        this.user = await userApi.getCurrentUser()
      } catch (error) {
        console.error('获取用户信息失败', error)
        this.logout()
      } finally {
        this.loading = false
      }
    },
    
    // 退出登录
    logout() {
      this.user = null
      this.token = ''
      localStorage.removeItem('token')
      router.push('/auth/login')
      ElMessage.success('已退出登录')
    }
  }
}) 