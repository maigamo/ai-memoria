#!/usr/bin/env python3
"""
AI-Memoria 后端服务启动脚本
提供命令行参数来配置服务器
"""

import argparse
import subprocess
import sys
import os
import socket
from dotenv import load_dotenv


def get_local_ip():
    """获取本机IP地址"""
    try:
        # 通过连接外部服务器获取本机IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        # 如果连接失败，则返回localhost
        return "127.0.0.1"


def main():
    # 加载环境变量
    load_dotenv()
    
    # 获取本机IP
    local_ip = get_local_ip()
    
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="AI-Memoria 后端服务启动脚本")
    parser.add_argument("--host", type=str, default=os.getenv("HOST", "0.0.0.0"),
                        help="服务器监听地址 (默认: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=int(os.getenv("PORT", "10012")),
                        help="服务器监听端口 (默认: 10012)")
    parser.add_argument("--reload", action="store_true", 
                        help="启用热重载 (开发模式)")
    parser.add_argument("--cors", type=str, default=None,
                        help="允许的CORS来源 (例如: http://192.168.1.100:10011,http://localhost:10011)")
    
    args = parser.parse_args()
    
    # 显示启动信息
    print(f"本机IP地址: {local_ip}")
    print(f"服务启动于: http://{local_ip if args.host == '0.0.0.0' else args.host}:{args.port}")
    
    # 设置环境变量
    env_vars = os.environ.copy()
    
    # 如果提供了CORS配置，设置环境变量
    if args.cors:
        env_vars["BACKEND_CORS_ORIGINS"] = args.cors
    else:
        # 否则使用默认配置并添加本机IP
        backends = [
            "http://localhost:10011",
            "http://127.0.0.1:10011",
            f"http://{local_ip}:10011"
        ]
        env_vars["BACKEND_CORS_ORIGINS"] = f"[{', '.join([f'\"'+b+'\"' for b in backends])}]"
    
    # 配置uvicorn启动命令
    cmd = [
        sys.executable, "-m", "uvicorn", "main:app",
        "--host", args.host,
        "--port", str(args.port)
    ]
    
    if args.reload:
        cmd.append("--reload")
    
    # 启动服务器
    try:
        subprocess.run(cmd, env=env_vars)
    except KeyboardInterrupt:
        print("服务器已停止")
    

if __name__ == "__main__":
    main()