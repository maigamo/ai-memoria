export interface User {
  id: string;
  email: string;
  full_name?: string;
}

export interface UserLogin {
  email: string;
  password: string;
}

export interface UserRegister {
  email: string;
  password: string;
  full_name?: string;
}

export interface UserUpdate {
  email?: string;
  full_name?: string;
  password?: string;
}

export interface Token {
  access_token: string;
  token_type: string;
} 