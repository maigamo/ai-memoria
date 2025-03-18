# AI Memoria 前端

AI Memoria 的前端项目，基于 Vue 3 + Vite + TypeScript + Element Plus 构建。

## 功能特性

- 响应式设计，支持桌面端和移动端
- 深色/浅色模式支持
- 用户认证系统（注册、登录、退出）
- GitHub 风格的 UI 设计
- PWA 支持

## 开发环境设置

### 安装依赖

```bash
npm install
```

### 启动开发服务器

```bash
npm run dev
```

默认将在 [http://localhost:10011](http://localhost:10011) 启动。

### 构建生产版本

```bash
npm run build
```

## 项目结构

```
frontend/
├── src/                   # 源代码
│   ├── assets/            # 静态资源
│   ├── components/        # 组件
│   ├── composables/       # 组合式 API
│   ├── layouts/           # 布局组件
│   ├── pages/             # 页面组件
│   ├── router/            # 路由配置
│   ├── stores/            # 状态管理
│   ├── styles/            # 样式文件
│   ├── types/             # TypeScript 类型
│   ├── utils/             # 工具函数
│   ├── App.vue            # 根组件
│   └── main.ts            # 入口文件
├── public/                # 公共资源
├── index.html             # HTML 模板
├── vite.config.ts         # Vite 配置
└── tsconfig.json          # TypeScript 配置
```

## 环境变量

复制 `.env.example` 到 `.env.local` 并根据需要修改：

```
VITE_API_BASE_URL=http://localhost:10012  # 后端 API 地址
VITE_APP_TITLE=AI Memoria                 # 应用名称
``` 