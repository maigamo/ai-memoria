# AI-Memoria - 智能记忆管理系统

AI-Memoria 是一个基于 AI 的个人知识管理系统，支持本地和云端存储，并提供智能搜索和分析功能。

## 🌟 主要特性

- 📝 多形式内容录入（文本、图片、音频）
- 🤖 智能意图识别（支持多种 LLM）
- 🔍 语义检索与内容分析
- 💾 在线/离线混合存储
- 📱 响应式界面设计
- 🔄 自动同步机制
- 🔒 隐私保护

## 🛠 技术栈

### 前端
- Vue 3 + Vite
- Element Plus
- PWA 支持

### 后端
- FastAPI
- SQLite（本地存储）
- PostgreSQL（云端存储）
- Weaviate（向量数据库）
- WebSocket

## 🚀 快速开始

### 环境要求
- Node.js >= 18
- Python >= 3.10
- PostgreSQL >= 14
- Weaviate

### 本地开发

1. 克隆仓库
\`\`\`bash
git clone https://github.com/maigamo/ai-memoria.git
cd ai-memoria
\`\`\`

2. 安装前端依赖
\`\`\`bash
cd frontend
npm install
\`\`\`

3. 安装后端依赖
\`\`\`bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
\`\`\`

4. 配置环境变量
\`\`\`bash
# 前端 (.env.local)
cp .env.example .env.local

# 后端 (.env)
cp .env.example .env
\`\`\`

5. 启动开发服务器
\`\`\`bash
# 前端
npm run dev

# 后端
uvicorn main:app --reload
uvicorn main:app --host 0.0.0.0 --port 10012 --reload
\`\`\`

## 📁 项目结构

\`\`\`
ai-memoria/
├── frontend/                # 前端项目
│   ├── src/                 # 源代码
│   │   ├── assets/          # 资源（图片、字体、CSS等）
│   │   ├── components/      # 组件（可复用的 UI 组件）
│   │   ├── composables/     # 组合式 API（封装的逻辑函数）
│   │   ├── layouts/         # 页面布局组件
│   │   ├── pages/           # 页面级组件（符合 Vue Router 约定式路由）
│   │   ├── router/          # 路由配置
│   │   ├── stores/          # 状态管理（Pinia）
│   │   ├── utils/           # 工具函数
│   │   ├── types/           # TypeScript 类型声明（如果使用 TS）
│   │   ├── config/          # 全局配置（如 API 地址、环境变量等）
│   │   ├── plugins/         # 第三方插件集成（如 Element Plus、Axios）
│   │   ├── main.ts          # 入口文件
│   │   ├── App.vue          # 根组件
│   ├── index.html           # 入口 HTML 文件
│   ├── vite.config.ts       # Vite 配置文件
│   ├── tsconfig.json        # TypeScript 配置文件（如果使用 TS）
│   ├── package.json         # 依赖管理
│   ├── README.md            # 项目说明文档
├── backend/                # FastAPI 后端项目
│   ├── requirements.txt    # Python 依赖包
│   ├── data/                # SQLite 数据库文件位于此处
│   ├── app/                # 主应用目录
│   │   ├── api/            # API 路由
│   │   │   ├── v1/         # API 版本管理（v1 版本）
│   │   │   ├── dependencies.py  # 依赖项（如数据库、认证）
│   │   ├── core/           # 核心功能（配置、日志）
│   │   │   ├── config.py   # 配置管理
│   │   │   ├── security.py # 安全/认证逻辑（如 OAuth2、JWT）
│   │   │   ├── logger.py   # 日志管理
│   │   ├── db/             # 数据库相关
│   │   │   ├── models.py   # SQLAlchemy 模型定义
│   │   │   ├── session.py  # 数据库会话管理
│   │   │   ├── migrations/ # 数据库迁移
│   │   ├── services/       # 业务逻辑
│   │   │   ├── user.py     # 用户相关业务逻辑
│   │   │   ├── content.py  # 内容管理业务逻辑
│   │   ├── schemas/        # Pydantic 数据模型
│   │   ├── utils/          # 工具函数
│   │   ├── main.py         # FastAPI 入口文件
│   │   ├── dependencies.py # 全局依赖项
│   ├── .env                # 环境变量配置
│   ├── README.md           # 项目说明文档
└── docs/                  # 项目文档
\`\`\`

## 🤝 贡献指南

1. Fork 项目
2. 创建特性分支 (\`git checkout -b feature/AmazingFeature\`)
3. 提交更改 (\`git commit -m 'Add some AmazingFeature'\`)
4. 推送到分支 (\`git push origin feature/AmazingFeature\`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 📞 联系方式

- 项目负责人：[Your Name]
- Email：[your.email@example.com]
- GitHub Issues：[project-issues-link]

## 默认用户信息

系统初始化时会自动创建以下默认管理员用户：

- 邮箱：aimemoria@example.com
- 密码：admin123

首次登录后请立即修改密码。

## 配置说明

### 数据库配置

默认使用 SQLite 作为本地存储，数据库文件位于 `backend/data/ai_memoria.db`。

如需使用 PostgreSQL 进行云端存储，请修改 `backend/core/config.py` 中的数据库配置。

### 端口配置

- 前端服务默认端口：10011
- 后端服务默认端口：10012

## 开发计划

详见 [开发阶段规划](docs/DEVELOPMENT_PHASES.md) 