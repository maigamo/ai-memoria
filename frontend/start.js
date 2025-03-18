#!/usr/bin/env node

const { execSync } = require('child_process');
const fs = require('fs');
const os = require('os');
const path = require('path');
const { program } = require('commander');

// 定义命令行参数
program
  .option('-h, --host <host>', '指定服务器监听地址', '0.0.0.0')
  .option('-p, --port <port>', '指定服务器监听端口', '10011')
  .option('-b, --backend <url>', '指定后端API地址 (例如: http://192.168.1.100:10012)')
  .option('-n, --network-status', '显示网络连接状态组件')
  .parse(process.argv);

const options = program.opts();

// 获取本机IP地址
function getLocalIP() {
  const interfaces = os.networkInterfaces();
  for (const name of Object.keys(interfaces)) {
    for (const iface of interfaces[name]) {
      // 过滤出IPv4地址并且非内部地址
      if (iface.family === 'IPv4' && !iface.internal) {
        return iface.address;
      }
    }
  }
  return '127.0.0.1'; // 如果没有找到合适的IP地址，返回localhost
}

const localIP = getLocalIP();

// 生成环境变量
let envContent = '';

// 如果指定了后端地址，添加到环境变量
if (options.backend) {
  envContent += `VITE_API_BASE_URL=${options.backend}\n`;
  console.log(`使用后端API地址: ${options.backend}`);
} else {
  // 否则使用默认值（localIP + 10012）
  envContent += `VITE_API_BASE_URL=http://${localIP}:10012\n`;
  console.log(`使用默认后端API地址: http://${localIP}:10012`);
}

// 添加其他环境变量
envContent += `VITE_APP_TITLE=AI Memoria\n`;

// 设置网络状态组件显示配置
envContent += `VITE_SHOW_NETWORK_STATUS=${options.networkStatus ? 'true' : 'false'}\n`;
if (options.networkStatus) {
  console.log('网络连接状态组件: 已启用');
} else {
  console.log('网络连接状态组件: 已禁用');
}

// 写入临时的环境变量文件
fs.writeFileSync(path.join(__dirname, '.env.local'), envContent);

// 启动开发服务器
console.log(`前端服务启动在: http://${localIP}:${options.port}`);
try {
  execSync(`npm run dev -- --host ${options.host} --port ${options.port}`, { 
    stdio: 'inherit',
    cwd: __dirname
  });
} catch (error) {
  console.error('启动服务器失败:', error.message);
} 