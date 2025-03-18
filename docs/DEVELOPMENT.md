# AI-Memoria 开发指南

## 目录
1. [开发环境配置](#开发环境配置)
2. [项目架构](#项目架构)
3. [开发规范](#开发规范)
4. [数据库设计](#数据库设计)
5. [API 文档](#api-文档)
6. [部署指南](#部署指南)

## 开发环境配置

### 必要软件
- Node.js >= 18
- Python >= 3.10
- PostgreSQL >= 14
- Weaviate
- Docker & Docker Compose（用于开发环境）

### 推荐开发工具
- VS Code
- 推荐插件：
  - ESLint
  - Prettier
  - Tailwind CSS IntelliSense
  - Python
  - Docker

## 项目架构

### 前端架构（Next.js）

#### 目录结构
\`\`\`
frontend/
├── app/                    # 页面和路由
│   ├── (auth)/            # 认证相关页面
│   ├── dashboard/         # 主面板页面
│   └── layout.tsx         # 根布局
├── components/            # React 组件
│   ├── ui/               # 基础 UI 组件
│   ├── shared/           # 共享组件
│   └── features/         # 功能组件
├── lib/                  # 工具函数
│   ├── hooks/            # 自定义 hooks
│   ├── utils/            # 工具函数
│   └── api/              # API 调用
├── styles/               # 全局样式
└── types/                # TypeScript 类型定义
\`\`\`

#### 状态管理
- 使用 React Context 处理全局状态
- Zustand 用于复杂状态管理
- SWR 用于数据请求和缓存

### 后端架构（FastAPI）

#### 目录结构
\`\`\`
backend/
├── api/                  # API 路由
│   ├── v1/              # API v1 版本
│   └── deps.py          # 依赖注入
├── core/                # 核心功能
│   ├── config.py        # 配置
│   ├── security.py      # 安全相关
│   └── llm/            # LLM 集成
├── db/                  # 数据库
│   ├── models/         # SQLAlchemy 模型
│   ├── migrations/     # 数据库迁移
│   └── repositories/   # 数据访问层
├── services/           # 业务逻辑
│   ├── auth.py         # 认证服务
│   ├── content.py      # 内容服务
│   └── llm.py         # LLM 服务
└── tests/             # 测试用例
\`\`\`

## 开发规范

### Git 工作流
1. 主分支
   - \`main\`: 生产环境分支
   - \`develop\`: 开发环境分支
   
2. 功能分支命名
   - 功能: \`feature/xxx\`
   - 修复: \`fix/xxx\`
   - 优化: \`optimize/xxx\`

### 代码规范

#### 前端
- 使用 ESLint + Prettier
- 组件采用函数式组件
- 使用 TypeScript 类型注解
- 遵循 React Hooks 规范

#### 后端
- 遵循 PEP 8 规范
- 使用 Black 格式化代码
- 类型注解必须
- 编写单元测试

## 数据库设计

### PostgreSQL 表结构

1. users
\`\`\`sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
\`\`\`

2. content
\`\`\`sql
CREATE TABLE content (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    type VARCHAR(50) NOT NULL,
    title TEXT,
    content TEXT,
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
\`\`\`

3. categories
\`\`\`sql
CREATE TABLE categories (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
\`\`\`

### Weaviate 模式
\`\`\`json
{
  "class": "Content",
  "properties": [
    {
      "name": "content_id",
      "dataType": ["string"]
    },
    {
      "name": "text",
      "dataType": ["text"]
    },
    {
      "name": "embedding",
      "dataType": ["vector"]
    }
  ]
}
\`\`\`

## API 文档

### 认证相关
- POST /api/v1/auth/register
- POST /api/v1/auth/login
- POST /api/v1/auth/refresh-token

### 内容管理
- POST /api/v1/content
- GET /api/v1/content
- PUT /api/v1/content/{id}
- DELETE /api/v1/content/{id}

### 分类管理
- POST /api/v1/categories
- GET /api/v1/categories
- PUT /api/v1/categories/{id}
- DELETE /api/v1/categories/{id}

### LLM 相关
- POST /api/v1/llm/analyze
- POST /api/v1/llm/search
- GET /api/v1/llm/models

## 部署指南

### 开发环境
1. 使用 Docker Compose 启动服务
\`\`\`bash
docker-compose -f docker-compose.dev.yml up
\`\`\`

### 生产环境
1. 构建 Docker 镜像
\`\`\`bash
docker build -t ai-memoria-frontend ./frontend
docker build -t ai-memoria-backend ./backend
\`\`\`

2. 使用 Docker Compose 部署
\`\`\`bash
docker-compose -f docker-compose.prod.yml up -d
\`\`\`

### 环境变量配置
- \`.env.production\`: 生产环境配置
- \`.env.development\`: 开发环境配置
- \`.env.local\`: 本地开发配置 