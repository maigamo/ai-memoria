# AI-Memoria 网络配置指南

本文档说明如何配置 AI-Memoria 的前端和后端服务连接。

## 自动识别本机IP

AI-Memoria 在启动时会自动识别本机IP地址，并使用以下默认配置：

- 前端服务: `http://<本机IP>:10011`
- 后端服务: `http://<本机IP>:10012`

## 前端配置

### 方法1: 使用启动脚本 (推荐)

项目提供了一个方便的启动脚本，可以自动配置网络设置：

```bash
# 进入前端目录
cd frontend

# 安装 commander 依赖
npm install commander

# 使用默认配置启动
npm run start

# 或者指定参数启动
npm run start -- --port 3000 --backend http://192.168.1.100:8000 --network-status
```

#### 可用命令行参数

- `-h, --host <host>`: 指定服务器监听地址 (默认: 0.0.0.0)
- `-p, --port <port>`: 指定服务器监听端口 (默认: 10011)
- `-b, --backend <url>`: 指定后端API地址 (例如: http://192.168.1.100:10012)
- `-n, --network-status`: 启用网络连接状态组件显示 (默认关闭)

### 方法2: 使用环境变量

你也可以通过编辑 `.env.local` 文件来配置前端：

```
# .env.local
VITE_API_BASE_URL=http://your-backend-ip:10012
VITE_APP_TITLE=AI Memoria
VITE_SHOW_NETWORK_STATUS=true
```

然后正常启动开发服务器：

```bash
npm run dev
```

## 后端配置

### 方法1: 使用启动脚本 (推荐)

后端也提供了启动脚本以方便配置：

```bash
# 进入后端目录
cd backend

# 使用默认配置启动
python start.py

# 或者指定参数启动
python start.py --port 8000 --reload --cors "http://192.168.1.100:3000"
```

#### 可用命令行参数

- `--host <host>`: 指定服务器监听地址 (默认: 0.0.0.0)
- `--port <port>`: 指定服务器监听端口 (默认: 10012)
- `--reload`: 启用热重载 (开发模式)
- `--cors <origins>`: 允许的CORS来源，用逗号分隔 (例如: http://192.168.1.100:3000,http://localhost:3000)

### 方法2: 使用环境变量

编辑 `.env` 文件：

```
# .env
HOST=0.0.0.0
PORT=10012
BACKEND_CORS_ORIGINS=["http://localhost:10011", "http://127.0.0.1:10011", "http://192.168.1.100:10011"]
```

然后正常启动：

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 10012 --reload
```

### 方法3: 命令行参数

也可以直接向 main.py 传递命令行参数：

```bash
python main.py --host 0.0.0.0 --port 10012
```

## 网络状态监控

AI-Memoria 提供了一个网络连接状态组件，用于显示前后端连接情况。**默认情况下该组件是关闭的**，但你可以通过配置来启用它。

### 启用网络状态组件

1. 通过命令行参数启用：
   ```bash
   npm run start -- --network-status
   ```

2. 通过环境变量启用：
   ```
   VITE_SHOW_NETWORK_STATUS=true
   ```

### 网络状态组件显示的信息

启用后，在开发环境中会显示一个网络状态监控组件，可以查看当前的连接情况：

- 前端地址
- 后端地址
- API基础URL
- 连接状态

这可以帮助你确认网络配置是否正确。

## 故障排除

如果遇到连接问题，请检查：

1. 防火墙是否允许指定端口通过
2. 前端与后端是否在同一网络中
3. CORS配置是否正确
4. 本机IP是否正确识别

如果有多个网络接口，系统会选择第一个非内部的IPv4地址。如果这不是你想要的，请手动指定IP地址。 