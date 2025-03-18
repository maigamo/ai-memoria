import http from './http'
import type { User, UserLogin, UserRegister, UserUpdate, Token } from '@/types/api'

/**
 * 认证相关API
 */
export const authApi = {
  // 用户登录
  login: (data: UserLogin) => http.post<Token>('/api/v1/auth/login', data),
  
  // 用户注册
  register: (data: UserRegister) => http.post<User>('/api/v1/auth/register', data),
}

/**
 * 用户相关API
 */
export const userApi = {
  // 获取当前用户信息
  getCurrentUser: () => http.get<User>('/api/v1/users/me'),
  
  // 更新当前用户信息
  updateCurrentUser: (data: UserUpdate) => http.put<User>('/api/v1/users/me', data),
} 